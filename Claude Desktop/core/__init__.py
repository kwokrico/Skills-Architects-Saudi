"""
Core logic package for the Saudi Architect skill suite.

Contains small, deterministic calculators used by the dispatcher.
"""

from .calculators import (
    run_calculation
)

VERSION = "1.0.0"

# This defines what is exported when someone runs 'from core import *'
__all__ = [
    "run_calculation"
]