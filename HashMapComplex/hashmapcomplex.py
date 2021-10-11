

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMapComplex:

    def __init__(self, size=50):
        self._size = size
        # # initialize hashing function
        # self._hash_function = lambda x: hash(x) % self._size
        # current amount of the elements in array
        self._filled = 0
        # initialize and repopulate list of length size given in constructor
        self.items = [None] * self._size

    def hash_function(self,key):
        if isinstance(key, str):
            hashed = [ord(_) for _ in key]
            return sum(hashed) % self._size
        elif isinstance(key, int):
            return (key * 2654435761) % (2 ** 3)
        else:
            raise ValueError("input should be integer or string")

    def add(self, key, value):
        self._filled += 1
        index = self.hash_function(key)
        node = self.items[index]
        # if empty:
        if node is None:
            self.items[index] = Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next

        node = Node(key, value)
        prev.next = node

    def get(self, key):
        index = self.hash_function(key)
        node = self.items[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node

    def remove(self, key):
        index = self.hash_function(key)
        node = self.items[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self._filled -= 1
            result = node.value
            if prev is None:
                self.items[index] = node.next
            else:
                prev.next = prev.next.next

            return result














