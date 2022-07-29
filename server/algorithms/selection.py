def selection_sort(arr):
    print(f'Given array to the sorting algo : {arr}')
    # in place, not stable, has to go through all even if partially sorted
    # time: O(n^2), space: O(1)
    # traverse through the elements
    for index1 in range(len(arr)):
        # find the minimum
        currMinIndex = index1
        # go through the rest of the array to find it
        for index2 in range(index1 + 1, len(arr)):
            if arr[currMinIndex] > arr[index2]:
                currMinIndex = index2
        # swap the minimum with the current element
        arr[index1], arr[currMinIndex] = arr[currMinIndex], arr[index1]
        # return the sorted array
    return arr