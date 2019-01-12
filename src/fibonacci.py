def fibo(iterations):
    items = [0, 1]
    for i in range(iterations - 2):
        items.append(items[i] + items[i + 1])
    return items

def fiboRecursiveAux(x, y, items, iterations):
    items.append(x)
    if len(items) == iterations:
        return
    fiboRecursiveAux(y, x + y, items, iterations)


def fiboRecursive(iterations):
    items = []
    fiboRecursiveAux(0, 1, items, 20)
    return items    

print(fibo(20))
print(fiboRecursive(20))