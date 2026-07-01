"""Deterministic calculators for saudi-architect-master (proxy / advisory only)."""

from __future__ import annotations

import math
from typing import Any


def _egress_diagonal_proxy(data: dict[str, Any]) -> dict[str, Any]:
    length = float(data.get("length", 0))
    width = float(data.get("width", 0))
    if length <= 0 or width <= 0:
        return {"error": "length and width must be positive (metres)"}
    diagonal = math.sqrt(length**2 + width**2)
    result: dict[str, Any] = {
        "calc_type": "egress_1004_7",
        "diagonal_proxy_m": round(diagonal, 3),
        "note": "Geometric proxy only — not path travel distance per SBC 501",
    }
    limit = data.get("limit_m")
    if limit is not None:
        limit_f = float(limit)
        result["limit_m"] = limit_f
        result["within_limit"] = diagonal <= limit_f
    return result


def _gfa_aggregator(data: Any) -> dict[str, Any]:
    if not isinstance(data, list):
        return {"error": "data must be a list of {area, is_exempt} objects"}
    total = 0.0
    accountable = 0.0
    exempt = 0.0
    rows = []
    for i, item in enumerate(data):
        if not isinstance(item, dict) or "area" not in item:
            return {"error": f"row {i}: expected {{area, is_exempt?}}"}
        area = float(item["area"])
        is_exempt = bool(item.get("is_exempt", False))
        total += area
        if is_exempt:
            exempt += area
        else:
            accountable += area
        rows.append({"area": area, "is_exempt": is_exempt})
    return {
        "calc_type": "gfa_aggregator",
        "total_m2": round(total, 2),
        "accountable_gfa_m2": round(accountable, 2),
        "exempt_m2": round(exempt, 2),
        "rows": rows,
        "note": "Confirm exempt areas against municipal survey / AHJ rules",
    }


def _u_value_from_layers(data: Any) -> dict[str, Any]:
    if not isinstance(data, list) or not data:
        return {"error": "data must be a non-empty list of {name, r} layers (m²K/W)"}
    r_total = 0.0
    layers = []
    for i, layer in enumerate(data):
        if not isinstance(layer, dict) or "r" not in layer:
            return {"error": f"layer {i}: expected {{name, r}}"}
        r_val = float(layer["r"])
        if r_val <= 0:
            return {"error": f"layer {i}: r must be positive"}
        r_total += r_val
        layers.append({"name": layer.get("name", f"layer_{i}"), "r": r_val})
    u = 1.0 / r_total
    return {
        "calc_type": "u_value_from_layers",
        "r_total_m2k_per_w": round(r_total, 4),
        "u_value_w_per_m2k": round(u, 4),
        "layers": layers,
        "note": "Compare to SBC 601 target for climate zone — verify edition",
    }


def _delta_t_check(data: dict[str, Any]) -> dict[str, Any]:
    t_in = float(data.get("t_inside_c", 24))
    t_out = float(data.get("t_outside_c", 46))
    delta = abs(t_out - t_in)
    return {
        "calc_type": "delta_t_check",
        "t_inside_c": t_in,
        "t_outside_c": t_out,
        "delta_t_c": round(delta, 2),
        "note": "High delta-T increases thermal movement risk — review expansion joints",
    }


def _layout_sort(data: Any) -> dict[str, Any]:
    if not isinstance(data, list):
        return {"error": "data must be a list of {id, area} or numeric areas"}
    items = []
    for i, item in enumerate(data):
        if isinstance(item, (int, float)):
            items.append({"id": str(i), "area": float(item)})
        elif isinstance(item, dict) and "area" in item:
            items.append({"id": str(item.get("id", i)), "area": float(item["area"])})
        else:
            return {"error": f"row {i}: expected number or {{id, area}}"}
    sorted_items = sorted(items, key=lambda x: x["area"], reverse=True)
    return {"calc_type": "layout_sort", "sorted": sorted_items}


# SBC 501 Table 1004.1.2 style occupant load factors (proxy — verify edition)
_OCCUPANCY_LOAD_FACTORS: dict[str, float] = {
    "assembly": 1.4,  # m² per person (proxy)
    "business": 9.3,
    "educational": 1.9,
    "factory": 9.3,
    "residential": 18.5,
    "storage": 27.9,
    "mercantile": 2.8,
    "utility": 18.5,
}


def _occupancy_load(data: dict[str, Any]) -> dict[str, Any]:
    area = float(data.get("area_m2", 0))
    use = str(data.get("use_type", "business")).lower()
    if area <= 0:
        return {"error": "area_m2 must be positive"}
    factor = _OCCUPANCY_LOAD_FACTORS.get(use)
    if factor is None:
        return {
            "error": f"unknown use_type '{use}'",
            "allowed": list(_OCCUPANCY_LOAD_FACTORS.keys()),
        }
    occupants = math.ceil(area / factor)
    return {
        "calc_type": "occupancy_load",
        "area_m2": area,
        "use_type": use,
        "load_factor_m2_per_person": factor,
        "occupant_load_persons": occupants,
        "note": "Proxy factors — verify against current SBC 501 / stamped fire strategy",
    }


def _far_check(data: dict[str, Any]) -> dict[str, Any]:
    gfa = float(data.get("gfa_m2", 0))
    plot = float(data.get("plot_area_m2", 0))
    far_limit = data.get("far_limit")
    if gfa <= 0 or plot <= 0:
        return {"error": "gfa_m2 and plot_area_m2 must be positive"}
    far = gfa / plot
    result: dict[str, Any] = {
        "calc_type": "far_check",
        "gfa_m2": gfa,
        "plot_area_m2": plot,
        "far_calculated": round(far, 4),
        "note": "Confirm FAR limit from organizational survey / masterplan",
    }
    if far_limit is not None:
        limit = float(far_limit)
        result["far_limit"] = limit
        result["within_limit"] = far <= limit
        result["headroom_m2"] = round(max(0, (limit * plot) - gfa), 2)
    return result


_CALCULATORS = {
    "egress_1004_7": _egress_diagonal_proxy,
    "egress_diagonal_proxy": _egress_diagonal_proxy,
    "gfa_aggregator": _gfa_aggregator,
    "u_value_from_layers": _u_value_from_layers,
    "delta_t_check": _delta_t_check,
    "layout_sort": _layout_sort,
    "occupancy_load": _occupancy_load,
    "far_check": _far_check,
}


def run_calculation(calc_type: str, data: Any = None) -> dict[str, Any]:
    if not calc_type:
        return {"error": "calc_type is required", "available": list(_CALCULATORS.keys())}
    fn = _CALCULATORS.get(calc_type)
    if not fn:
        return {"error": f"Unknown calc_type: {calc_type}", "available": list(_CALCULATORS.keys())}
    if data is None:
        data = {} if calc_type in ("egress_1004_7", "egress_diagonal_proxy", "delta_t_check", "occupancy_load", "far_check") else []
    try:
        return fn(data)
    except (TypeError, ValueError) as e:
        return {"error": f"Invalid input: {e}"}
