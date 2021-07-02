def array_sign(nums):
    if 0 in nums:
        return 0

    negatives = len([i for i in nums if i < 0])
    if negatives % 2 == 0:
        return 1

    return -1


def array_sign_oneshot(nums):
    negative = False

    for i in nums:
        if i == 0:
            return 0
        if i < 0:
            negative = not negative

    return -1 if negative else 1

