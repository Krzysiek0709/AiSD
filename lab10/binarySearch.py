from array import array
from ctypes import Array
from typing import Tuple


def binary_search(numbers: Array, value: int) -> Tuple[bool, int]:
    element_found = False
    left = 0
    right = len(ints)
    while left <= right:
        middle = (left + right) // 2
        if ints[middle] == num:
            element_found = True
            find_equal_neighbours(ints, middle)
            break
        elif ints[middle] < num:
            left = middle + 1
        else:
            right = middle - 1
    if not element_found:
        print('Nie znaleziono elementu')

def find_equal_neighbours(ints, index):
    low_index = index
    high_index = index
    value = ints[index]
    while low_index - 1 >= 0 and ints[low_index - 1] == value:
        low_index -= 1
    while high_index + 1 < len(ints) and ints[high_index + 1] == value:
        high_index += 1
    for i in range(low_index, high_index + 1):
        print('Numer zostal znaleziony w indeksie:', i)


ints = [1, 5, 6, 7, 10, 26, 29, 40]
num = 29
num2 = 5
binary_search(ints, num)
