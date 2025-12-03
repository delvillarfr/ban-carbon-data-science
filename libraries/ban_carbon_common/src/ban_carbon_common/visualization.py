"""
Shared visualization utilities.

This module provides reusable plotting functions for geographic
and statistical visualizations.
"""

import matplotlib.pyplot as plt


def setup_map_figure(figsize=(12, 12), background_color="black"):
    """
    Create a matplotlib figure configured for mapping.

    Args:
        figsize: Figure size as (width, height) tuple
        background_color: Background color for figure and axes

    Returns:
        Tuple of (figure, axes)
    """
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor(background_color)
    ax.set_facecolor(background_color)
    ax.axis("off")
    return fig, ax


__all__ = [
    "setup_map_figure",
]
