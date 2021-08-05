def selection_sort(target: [int]) -> [int]:
    for i in range(len(target)):
        low_index = i
        for j in range(i + 1, len(target)):
            if target[low_index] > target[j]:
                target[low_index], target[j] = target[j], target[low_index]

    return target


if __name__ == '__main__':
    print(selection_sort([3, 1, 4, 6, 10, 123, 2, 7]))
