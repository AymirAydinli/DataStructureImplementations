class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def add_front(self, data):
        node = Node(data)
        node.next = self.head
        self.head.prev = node
        self.head = node

    def add_last(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node
        node.prev = last

    def search(self, data):
        last = self.head
        while last is not None:
            if last.data == data:
                return True
                break
            last = last.next
        return False

    def remove(self, data):
        nodeH = self.head
        if nodeH is not None:
            if nodeH.data == data:
                self.head = nodeH.next
                nodeH = None
                return
        while nodeH is not None:
            if nodeH.data == data:
                break
            nodeH = nodeH.next

        nodeH.next.prev = nodeH.prev
        nodeH.prev.next = nodeH.next
        nodeH = None

    def printForward(self):
        items = []
        last = self.head
        while last is not None:
            items.append(last.data)
            last = last.next
        return items

    def printBackward(self):
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

