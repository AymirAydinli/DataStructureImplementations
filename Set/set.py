class Set:
    # ration of element to size of array on which it should be upsized
    RESIZE_FACTOR_UP = 1 / 2

    # ration of element to size of array on which it should be downsized
    RESIZE_FACTOR_DOWN = 1 / 3

    # minimal size of array(the size should not be shrank below this size)
    MIN_SIZE = 10

    def __init__(self, size=10):
        self.size = size
        self._filled = 0
        self._element = [[] for _ in range(size)]

    def hash_function(self, value):
        if isinstance(value, str):
            hashed = [ord(_) for _ in value]
            return sum(hashed) % self.size
        elif isinstance(value, int):
            return (value * 2654435761) % (2 ** 3)
        else:
            raise ValueError("input should be integer or string")

    def _contains(self, value):
        for i, e in enumerate(self._element[self.hash_function(value)]):
            if value == e:
                return i
        return -1

    def contains(self, value):
        return self._contains(value) >= 0

    def add(self, value):
        if not self.contains(value):
            self._filled += 1
        self._element[self.hash_function(value)].append(value)
        self._resize

    def delete(self, value):
        # decrement amount of elements if you  remove element that existed
        index = self._contains(value)
        if index >= 0:
            self._filled -= 1
            self._element[self.hash_function(value)].pop(index)
            self._resize()

    def _resize(self):
        capacity_ratio = float(self._filled) / self.size
        # shrink away if if there is less than RESIZE_FACTOR_DOWN
        if capacity_ratio < Set.RESIZE_FACTOR_DOWN and self.size / 2 >= Set.MIN_SIZE:
            self._create_resized_array(self.size // 2)
        if capacity_ratio > Set.RESIZE_FACTOR_UP:
            self._create_resized_array(self.size * 2)

    def _create_resized_array(self, new_size):
        new_element_array = [[] for _ in range(new_size)]
        self.size = new_size
        for l in self._element:
            for e in l:
                # uses new function
                new_element_array[self.hash_function(e)].append(e)
        self._element = new_element_array

    def __iter__(self):
        for l in self._element:
            if l:
                for e in l:
                    yield l
        raise StopIteration()

    def __str__(self):
        return f"size: {self.size} and elements: {self._element}"
