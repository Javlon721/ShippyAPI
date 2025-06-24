def bin_search(arr, target, check):
    left = 0
    right = len(arr)
    while left < right:
        m = (left + right) // 2
        if check(m, arr, target):
            right = m
        else:
            left = m + 1
    return left
