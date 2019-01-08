def search(list, item):
    first = 0
    last = len(list) - 1
    step = 0

    while first <= last:
        mid = (last + first) // 2
        guess = list[mid]
        step += 1
        
        if guess == item:
            return (mid, step)
        if guess > item:
            last = mid - 1
        else:
            first = mid + 1        
    
    return None

my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

position, step = search(my_list, 11)
print("Item 7 was found on #" + `position` + " with " + `step` + " steps")

position, step = search(my_list, 21)
print("Item 21 was found on #" + `position` + " with " + `step` + " steps")