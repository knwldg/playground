def two_sum(nums: [int], target: int):
    for (index, n) in enumerate(nums):
        for (second_index, m) in enumerate(nums):
            if index == second_index:
                continue
            if n + m == target:
                return [index, second_index]


if __name__ == '__main__':
    print(two_sum([1, 3, 5], 8))
