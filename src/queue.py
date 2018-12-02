class QueueItem:
    nextItem = None
    value = ""

    def __init__(self, value):
        self.value = value

class Queue:
    firstItem = None
    lastItem = None
    size = 0

    def enqueue(self, value):
        item = QueueItem(value)
        if self.firstItem == None:
            self.firstItem = item
            self.lastItem = item
        else:
            self.lastItem.nextItem = item
            self.lastItem = item

        self.size += 1
    
    def dequeue(self):
        if self.firstItem == None:
            return None
        else:
            temp = self.firstItem
            self.firstItem = self.firstItem.nextItem
            self.size -= 1
            return temp.value

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

queue = Queue()
queue.show()
print("Enqueueing items...")
queue.enqueue("dog")
queue.enqueue("cat")
queue.enqueue("bird")
queue.show()
print("The queue size now is: " + `queue.size`)
print("Dequeuing: " + queue.dequeue())
print("Dequeuing: " + queue.dequeue())
print("The queue size now is: " + `queue.size`)
queue.show()
print("Dequeuing: " + queue.dequeue())
print("The queue size now is: " + `queue.size`)
queue.show()