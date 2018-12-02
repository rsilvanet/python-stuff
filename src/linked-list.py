class LinkedItem:
    nextItem = None
    value = ""

    def __init__(self, value):
        self.value = value

class LinkedList:
    firstItem = None
    lastItem = None
    size = 0

    def add(self, value):
        item = LinkedItem(value)
        if self.firstItem == None:
            self.firstItem = item
            self.lastItem = item
        else:
            self.lastItem.nextItem = item
            self.lastItem = item
        self.size += 1 
    
    def show(self):
        if self.firstItem == None:
            print("Empty")
            return
        else:
            currentItem = self.firstItem
            content = "start -> " + currentItem.value + " -> "
            while currentItem.nextItem != None:
                currentItem = currentItem.nextItem
                content += currentItem.value + " -> "
            content += "end"
        print(content)

    def get(self, index):
        currentItem = self.firstItem
        currentIndex = 0
        while currentItem != None:
            if (currentIndex == index):
                return currentItem.value
            currentItem = currentItem.nextItem
            currentIndex += 1
        return None

list = LinkedList()
list.show()
print("Adding items...")
list.add("dog")
list.add("cat")
list.add("bird")
list.add("fish")
list.show()
print("The #1 item is: " + list.get(1))
print("The #3 item is: " + list.get(3))