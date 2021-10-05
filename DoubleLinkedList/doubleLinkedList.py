class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_front(self, data):
        node = Node(data)
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.size += 1

    def add_last(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.size += 1
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node
        node.prev = last

        self.size += 1

    def search(self, data):
        last = self.head
        while last:
            if last.data == data:
                return last
            last = last.next
        raise Exception("Element not found")


    def remove(self, data):
        node_tbd = self.head
        if node_tbd is not None:
            if node_tbd.data == data:
                self.head = node_tbd.next
                node_tbd = None
                return
        while node_tbd is not None:
            if node_tbd.data == data:
                break
            node_tbd = node_tbd.next

        node_tbd.next.prev = node_tbd.prev
        node_tbd.prev.next = node_tbd.next
        node_tbd = None
        self.size -= 1

    def to_array(self):
        items = []
        last = self.head
        while last is not None:
            items.append(last.data)
            last = last.next
        return items

    def to_reverse_array(self):
        items = []
        last = self.head
        while last.next is not None:
            last = last.next
        while last is not None:
            items.append(last.data)
            last = last.prev
        return items

    def add_after(self, item, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        target = self.head
        while target:
            if target.data == item:
                break
            target = target.next
        node.next = target.next
        node.prev = target
        target.next.prev = node
        target.next = node
        self.size += 1

    def add_before(self, item, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        target = self.head
        while target:
            if target.data == item:
                break
            target = target.next
        node.next = target
        node.prev = target.prev
        target.prev.next = node
        target.prev = node
        self.size += 1
