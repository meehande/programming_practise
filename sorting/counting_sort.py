from typing import List, Callable
import numpy as np
"""
input array of numbers + range
create frequency array of the input
-> that gives the sorted output

Different to comparison sorts, where the O(n) is at best O(nlogn)


The complexity of counting sort is:
 O(n+k) time and O(n+k) space, where k = number of possible values
- if k is much smaller than n, this goes to O(n)


"""


def sort(values: List[int], max_value: int = 10):
    frequency = np.array([0] * (max_value+1))
    for v in values:
        frequency[v] += 1
    res = []
    for v, count in enumerate(frequency):
        res.extend([v]*count)
    return res


def object_sort(items: List[object], getter: Callable, max_value: int = 10):
    counts = np.array([0] * (max_value + 1))
    next_indx = np.array([0] * (max_value+1))

    for item in items:
        c = getter(item)
        counts[c] += 1

    for i in range(max_value):
        next_indx[i + 1] = next_indx[i] + counts[i]

    res = np.array([None]*len(items))
    for item in items:
        c = getter(item)
        idx = next_indx[c]
        res[idx] = item
        next_indx[c] += 1
    return res


s = object_sort([4, 8, 4, 2, 9, 9, 6, 2, 9], getter = lambda x: x )
s = sort([4, 8, 4, 2, 9, 9, 6, 2, 9])


