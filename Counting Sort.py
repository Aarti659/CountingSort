def countSort(array, max_val):
    M = max_val + 1
    count = [0] * M

    for b in array:

        count[b] += 1
    i = 0
    for b in range(M):
        for d in range(count[b]):
            array[i] = b
            i += 1
    return array


print(countSort([1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1], 7))



