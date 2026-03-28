def find_min_max(arr):
    if not arr:
        return None, None  # handle empty array

    min_val = max_val = arr[0]

    for num in arr[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return min_val, max_val


# Example usage
arr = [3, 5, 1, 9, 2, 8, 23]
minimum, maximum = find_min_max(arr)

print("Smallest:", minimum)
print("Largest:", maximum)