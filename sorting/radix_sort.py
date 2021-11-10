from typing import List, Union
import numpy as np
# TODO: make work for strings / ints (input the "alphabet" to the fn)

NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
LETTERS = 'abcdefghijklmnopqrstuvwxyz'


def _extract_bit(value: int, bit: int):
    mask = 1 << bit
    return value & mask


def _counting_sort(values, bit):
    counts = np.array([0]*len(NUMBERS))
    new_indices = np.array([0]*len(NUMBERS))

    for v in values:
        bit_value = _extract_bit(v, bit)
        counts[bit_value] += 1

    res = np.array([None]*len(values))
    for v in values:
        bit_value = _extract_bit(v, bit)




def sort_lst(values: Union[List[int], str], alphabet=NUMBERS):
    buckets = np.array([None]*len(alphabet))




def sort(values: List[int]):
    pass


def sort_binary(values: List[int]):
    pass
