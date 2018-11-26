class LinkedItem:
    previousItem = None    
    nextItem = None
    value = ""

    def __init__(self, value):
        self.value = value

class LinkedList:
    firstItem = None
    lastItem = None
    size = 0

    def add(self, item):
        if self.firstItem == None:
            self.firstItem = item
            self.lastItem = item
        else:
            item.previous = self.lastItem
            self.lastItem.nextItem = item
            self.lastItem = item
        self.size += 1 
    
    def show(self):
        if self.firstItem == None:
            return "Empty"
        else:
            content = ""
            currentItem = self.firstItem
            content = currentItem.value + " -> "
            while currentItem.nextItem != None:
                currentItem = currentItem.nextItem
                content += currentItem.value
                if currentItem.nextItem != None:
                    content += " -> "
        print(content)

    def get(self, index):
        if self.firstItem == None:
            return None
        else:
            currentItem = self.firstItem
            currentIndex = 0
            while currentItem.nextItem != None:
                if (currentIndex == index):
                    return currentItem.value
                currentItem = currentItem.nextItem
                currentIndex += 1


list = LinkedList()
item1 = LinkedItem("dog")
item2 = LinkedItem("cat")
item3 = LinkedItem("bird")
list.add(item1)
list.add(item2)
list.add(item3)
list.show()
print(list.get(1))