class HashMap:
    def __init__(self, size):
        self.size = size
        self.items = [None for _ in range(size)]
        self.filled = 0

    def hash_function(self, index):
        if isinstance(index, str):
            hashed = [ord(_) for _ in index]
            return sum(hashed) % self.size
        elif isinstance(index, int):
            return (index * 2654435761) % (2 ** 3)
        else:
            raise ValueError("input should be integer or string")

    def add(self, index, value):

        if self.items[self.hash_function(index)] is not None:
            #raise Exception("Collision happened, please input a different index")
            self.items[self.hash_function(index)] = value
        else:
            self.items[self.hash_function(index)] = value
            self.filled += 1

    def get(self, index):
        if self.items[self.hash_function(index)] is not None:
            return self.items[self.hash_function(index)]
        else:
            raise Exception("Element don't exist")

    def remove(self, index):
        if self.items[self.hash_function(index)] is not None:
            self.items[self.hash_function(index)] = None
            self.filled -= 1
        else:
            raise ValueError("index is empty")

    def capacity(self):
        return len(self.items)


