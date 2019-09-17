def uglyMergeSort(array):
    swaps = 0
    comparisons = 0

    if len(array) > 1:

        middle = len(array) / 2
        
        leftArray = array[:int(middle)]
        rightArray = array[int(middle):]

        x, leftComparisons, leftSwaps = uglyMergeSort(leftArray)
        y, rightComparisons, rightSwaps = uglyMergeSort(rightArray)

        swaps += leftSwaps + rightSwaps
        comparisons += leftComparisons + rightComparisons

        leftIndex = 0
        rightIndex = 0
        arrayIndex = 0

        while leftIndex < len(leftArray) and rightIndex < len(rightArray):
            comparisons += 1
            if leftArray[leftIndex] < rightArray[rightIndex]:
                array[arrayIndex] = leftArray[leftIndex]
                leftIndex += 1
            else:
                array[arrayIndex] = rightArray[rightIndex]
                rightIndex += 1
                swaps += 1
            arrayIndex += 1

        while leftIndex < len(leftArray):
            array[arrayIndex] = leftArray[leftIndex]
            leftIndex += 1
            arrayIndex += 1

        while rightIndex < len(rightArray):
            array[arrayIndex] = rightArray[rightIndex]
            rightIndex += 1
            arrayIndex += 1

    return array, comparisons, swaps

array = [7, 1, 3, 8, 2, 5, 4, 6]
sortedArray, comparisons, swaps = uglyMergeSort(array)

print("Original:", array)
print("Sorted:", sortedArray)
print("Comparisons:", comparisons)
print("Swaps:", swaps)