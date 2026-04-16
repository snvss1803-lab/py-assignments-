class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(item, "added to queue")

    def dequeue(self):
        if len(self.items):
            print("Queue is empty")
        else:
            self.items.pop()
            print( "removed from queue")

    def peek(self):
        if len(self.items) ==0:
            print("Queue is empty")
        else:
            print("Front element is:", self.items)



q = Queue()
print("Queue created")


q.enqueue(90)
q.enqueue(40)
q.enqueue(17)
q.dequeue(40)
q.peek()
q.dequeue()
q.peek()
