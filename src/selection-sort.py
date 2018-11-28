def getIndexOfLower(array):
    lowerIndex = 0
    lowerValue = array[0]
    for i in range(1, len(array)):
        if array[i] < lowerValue:
            lowerIndex = i
            lowerValue = array[i]
    return lowerIndex

def sort(array):
    sortedArray = []
    for i in range(0,len(array)):
        indexOfLower = getIndexOfLower(array)
        valueOfLower = array.pop(indexOfLower)
        sortedArray.append(valueOfLower)
    return sortedArray

print(sort([3, 32, 5, 1, 9, 23, 15, 9, 10, 8, 1, 61, 47]))