array = [ 3, 5, 2, 9, 15, 7, 8 , 1, 12, 10, 2, 7 ]
inverting = True

while inverting:
    inverting = False
    for i in range(0, len(array) - 1):
        if array[i] > array[i+1]:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
            inverting = True

print(array)
