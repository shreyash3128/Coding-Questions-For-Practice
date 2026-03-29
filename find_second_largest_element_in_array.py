def find_second_largest(arr):
    if len(arr) < 2:
        return None #not enough elements
    first = second = 0
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('inf') else None

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Second Largest: ", find_second_largest(arr))