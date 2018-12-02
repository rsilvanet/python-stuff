class StackItem:
    nextItem = None
    value = ""

    def __init__(self, value):
        self.value = value

class Stack:
    topItem = None
    size = 0

    def push(self, value):
        item = StackItem(value)
        if self.topItem == None:
            self.topItem = item
        else:
            item.nextItem = self.topItem
            self.topItem = item
        self.size += 1
    
    def pop(self):
        if self.topItem == None:
            return None
        else:
            temp = self.topItem
            self.topItem = self.topItem.nextItem
            return temp.value
        self.size -= 1

    def show(self):
        if self.topItem == None:
            print("Empty")
            return
        else:
            currentItem = self.topItem
            content = "top -> " + currentItem.value + " -> "
            while currentItem.nextItem != None:
                currentItem = currentItem.nextItem
                content += currentItem.value + " -> "
            content += "bottom"
        print(content)

stack = Stack()
stack.push("dog")
stack.push("cat")
stack.push("bird")
stack.show()
print("Pop:" + stack.pop())
print("Pop:" + stack.pop())
stack.show()
print("Pop:" + stack.pop())
stack.show()