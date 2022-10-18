"""
Test MergeIntervals.
Authors: Andreas Lebedev, 10.2022.
"""

import pytest
from MergeIntervals import merge_intervals


def test_coding_task():
    """Example which were given in the coding task."""

    interval_test = [[25, 30], [2, 19], [14, 23], [4, 8]]
    assert merge_intervals(interval_test) == [[2, 23], [25, 30]]

def test_negative_interval():
    """Test with negative elements."""

    interval_test = [[25, 30], [-19, -2], [14, 23], [4, 8]]
    assert merge_intervals(interval_test) == [[-19, -2], [4, 8], [14, 23], [25, 30]]

def test_same_intervals():
    """Test with identical intervals."""

    interval_test = [[25, 30], [2, 19], [25, 30], [2, 19]]
    assert merge_intervals(interval_test) == [[2, 19], [25, 30]]




