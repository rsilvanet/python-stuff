def sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        lower = [i for i in array[1:] if i <= pivot]
        higher = [i for i in array[1:] if i > pivot]
        return sort(lower) + [pivot] + sort(higher)

print(sort([3, 32, 5, 1, 9, 23, 15, 9, 10, 8, 1, 61, 47]))