class HashMap:
    def __init__(self, size):
        self.size = size
        self.items = [None for _ in range(size)]
        self.filled = 0

    def hash_function(self, index):
        return hash(index) % self.size

    def add(self, index, value):

        if self.items[self.hash_function(index)] is not None:
            # raise ValueError("Collision happened, please input a different index")
            return "Collision happened, please input a different index"
        else:
            self.items[self.hash_function(index)] = value
            self.filled += 1

    def get(self, index):
        if self.items[self.hash_function(index)] is not None:
            return self.items[self.hash_function(index)]
        else:
            return "Empty"

    def remove(self, index):
        if self.items[self.hash_function(index)] is not None:
            self.items[self.hash_function(index)] = None
            self.filled -= 1
        else:
            # raise ValueError("index is already empty")
            return "index is already empty"

    def capacity(self):
        return "length is: " + str(len(self.items)) + " and filled is: " + str(self.filled)


if __name__ == "__main__":
    main()
