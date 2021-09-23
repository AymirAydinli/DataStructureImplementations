class Stack:
    def __init__(self):
        self.items = []

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def empty(self):
        return len(self.items) == 0
