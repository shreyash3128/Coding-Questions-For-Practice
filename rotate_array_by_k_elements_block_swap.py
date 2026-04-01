def swap(arr, start1, start2, size):
    for i in range(size):
        arr[start1 + i], arr[start2 + i] = arr[start2 + i], arr[start1 + i]


def left_rotate(arr, k, n):
    if k == 0 or k == n:
        return

    def block_swap(start, k, n):
        if k == 0 or k == n:
            return

        if k == n - k:
            swap(arr, start, start + n - k, k)
            return

        elif k < n - k:
            swap(arr, start, start + n - k, k)
            block_swap(start, k, n - k)

        else:
            swap(arr, start, start + k, n - k)
            block_swap(start + n - k, 2 * k - n, k)

    block_swap(0, k, n)


# Example
arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
left_rotate(arr, k, len(arr))
print("Rotated:", arr)