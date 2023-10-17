def lis(arr):
    n = len(arr)
    if n == 0:
        return []

    lis_lengths = [1] * n
    previous_indices = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis_lengths[i] < lis_lengths[j] + 1:
                lis_lengths[i] = lis_lengths[j] + 1
                previous_indices[i] = j

    max_length = max(lis_lengths)
    max_index = lis_lengths.index(max_length)

    lis_sequence = []
    while max_index >= 0:
        lis_sequence.insert(0, arr[max_index])
        max_index = previous_indices[max_index]

    return lis_sequence


# Example usage:
arr = [10, 22, 9, 33, 21, 50, 41, 60]
sequence = lis(arr)
print("LIS elements:", sequence)



