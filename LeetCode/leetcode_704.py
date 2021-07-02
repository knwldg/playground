from tools import time_function_ns


def regular_search(nums: [int], target: int) -> int:
    for index, i in enumerate(nums):
        if i == target:
            return index

    return -1


def binary_search(nums: [int], target: int) -> int:
    ret = -1

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = int((low + high) / 2)
        curr = nums[mid]

        if curr == target:
            return mid

        if target > curr:
            low = mid + 1

        if target < curr:
            high = mid - 1

    return ret


print(time_function_ns(regular_search, [-1, 0, 3, 5, 9, 12], 9))
print(time_function_ns(regular_search, [-1, 0, 3, 5, 9, 12], 2))

print(time_function_ns(binary_search, [-1, 0, 3, 5, 9, 12], 9))
print(time_function_ns(binary_search, [-1, 0, 3, 5, 9, 12], 2))
