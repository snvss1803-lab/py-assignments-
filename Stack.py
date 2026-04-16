class Stack:
    def __init__(self):
        self.items = [100,200,300,400]

    def push(self, item):
        self.items.append(item)
        print(item, "pushed into stack")

    def pop(self):
        if len(self.items) == 0:
            print("Stack is empty")
        else:
            self.items.pop()
            print( "popped from stack")

    def peek(self):
        if len(self.items) == 0:
            print("Stack is empty")
        else:
            print("Top element is:", self.items[-1])


s = Stack()

s.push(100)
s.push(90)

s.peek()
s.pop()
s.peek()
