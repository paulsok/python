def binary_search(arr, target):
    left_idx, right_idx = 0, len(arr)
    while left_idx < right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if arr[mid_idx] == target:
            return True
        elif arr[mid_idx] < target:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx
    return False
