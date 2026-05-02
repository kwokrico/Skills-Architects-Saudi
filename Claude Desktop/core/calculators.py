import math


class EgressCalculator:
    """
    Small helper calculations for egress sanity checks.

    Notes:
    - This module deliberately avoids jurisdiction-specific code quoting.
    - Use it to support quick checks and comparisons; the project’s SBC/SCD
      compliance must be validated against the applicable code edition and AHJ.
    """

    def calculate_remotest_point(self, data):
        """
        Computes the diagonal distance of a rectangular room as a proxy for a
        remotest-point travel distance upper-bound (not a substitute for path
        travel distance along actual routes).

        Expected keys in `data`:
        - length (m), width (m)
        - limit_m (optional): a user-supplied project limit to compare against
        """
        data = data or {}
        length = float(data.get("length", 0) or 0)
        width = float(data.get("width", 0) or 0)

        # Diagonal distance is often the start for remotest point assessment
        diagonal = math.sqrt(length ** 2 + width ** 2)

        limit_m = data.get("limit_m", None)
        status = None
        if limit_m is not None:
            limit_m = float(limit_m)
            status = "Pass" if diagonal <= limit_m else "Fail"

        return {
            "diagonal_distance": round(diagonal, 2),
            "limit_m": limit_m,
            "status": status,
            "note": "This is a geometric proxy only; measure egress travel distance along the actual route."
        }

    # Backwards-compatible alias for dispatcher expectations
    def calculate(self, data):
        return self.calculate_remotest_point(data)


class ThermalEnvelopeHelper:
    """
    Lightweight envelope sanity checks suitable for early KSA design coordination.
    """

    def u_value_from_layers(self, layers):
        """
        Computes U-value from a list of layers with R-values (m²K/W).
        Input example: [{\"name\": \"insulation\", \"r\": 2.5}, ...]
        """
        layers = layers or []
        r_total = 0.0
        for layer in layers:
            r_total += float(layer.get("r", 0) or 0)
        if r_total <= 0:
            return {"error": "Total R-value must be > 0."}
        u = 1.0 / r_total
        return {"r_total": round(r_total, 4), "u_value": round(u, 4)}

    def delta_t_check(self, t_inside_c, t_outside_c):
        """
        Computes delta-T to support glazing/façade discussions in hot climates.
        """
        ti = float(t_inside_c)
        to = float(t_outside_c)
        return {"delta_t_c": round(abs(to - ti), 2)}


class GFACalculator:
    """Generic floor area aggregation (jurisdiction-neutral)."""

    def aggregate_gfa(self, floor_data):
        """
        Expects floor_data: list of dicts with:
        - area (float)
        - category (string, optional)
        - is_exempt (bool, optional) for internal tracking (not code-claimed)
        """
        floor_data = floor_data or []
        total_gfa = 0
        exempt_gfa = 0

        for item in floor_data:
            area = item.get("area", 0)
            if item.get("is_exempt"):
                exempt_gfa += area
            else:
                total_gfa += area

        return {
            "total_gfa": round(total_gfa, 2),
            "exempt_gfa": round(exempt_gfa, 2),
            "accountable_gfa": round(total_gfa - exempt_gfa, 2)
        }


class DataSorter:
    """Logic for the 'Dictionary Sort' for OCR/Layout data."""

    def sort_by_layout(self, items):
        """
        Sorts a list of dictionaries based on 'x' and 'y' coordinates.
        Useful for architectural notes and accounting tables.
        """
        if not items or not isinstance(items, list):
            return []

        # Sort primarily by Y (top to bottom) then by X (left to right)
        # We use a 'tolerance' for Y to group items on the same line
        tolerance = 10

        sorted_items = sorted(
            items,
            key=lambda b: (b.get('y', 0) // tolerance, b.get('x', 0))
        )

        return sorted_items


def run_calculation(calc_type, data):
    """Factory function for the main.py dispatcher."""
    if calc_type == "egress_1004_7":
        return EgressCalculator().calculate_remotest_point(data)
    elif calc_type == "egress_diagonal_proxy":
        return EgressCalculator().calculate_remotest_point(data)
    elif calc_type == "gfa_aggregator":
        return GFACalculator().aggregate_gfa(data)
    elif calc_type == "u_value_from_layers":
        return ThermalEnvelopeHelper().u_value_from_layers(data)
    elif calc_type == "delta_t_check":
        return ThermalEnvelopeHelper().delta_t_check(
            (data or {}).get("t_inside_c", 24),
            (data or {}).get("t_outside_c", 46),
        )
    elif calc_type == "layout_sort":
        return DataSorter().sort_by_layout(data)
    else:
        return {"error": f"Calculator type {calc_type} not implemented."}