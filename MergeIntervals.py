"""
Merge list of intervals.
Authors: Andreas Lebedev, 10.2022.
"""

from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """ Function, which takes a list of intervals end returns a list of intervals, which are not overlapping.
    Assuming integers, input not empty list, and correct intervals -> no [9, 4]

    Parameters
    ----------
    intervals : List[List[int]])
        List of intervals.

    Returns
    -------
    List[List[int]]:
        List of intervals, which are not overlapping.

    Examples
    --------
    >>> interval_test = [[25, 30], [2, 19], [14, 23], [4, 8]]
    >>> merge_intervals(interval_test)
    [[2, 23], [25, 30]]

    """

    if len(intervals) == 1:
        return [intervals[0]]

    # sort the intervals based on the first value of each interval
    intervals_sorted = sorted(intervals, key=lambda x: x[0])
    intervals_return = [intervals_sorted[0]]

    for interv in intervals_sorted[1:]:
        # check if the two intervals are overlapping
        if interv[0] > intervals_return[-1][1]:
            intervals_return.append(interv)
        else:
            # check if interval is already contained
            if interv[1] > intervals_return[-1][1]:
                intervals_return[-1][1] = interv[1]

    return intervals_return


if __name__ == '__main__':
    interval_test = [[25, 30], [2, 19], [14, 23], [4, 8]]
    print(merge_intervals(interval_test))

    pass
