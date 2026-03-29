def find_second_smallest(arr):
    if len(arr) < 2:
        return None  # Not enough elements

    first = second = float('inf')

    for num in arr:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num

    return second if second != float('inf') else None


# Example
arr = [3, 5, 1, 9, 2, 1]
print("Second Smallest:", find_second_smallest(arr))