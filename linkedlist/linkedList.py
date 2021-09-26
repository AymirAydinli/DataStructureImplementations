class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0;

    def add_first(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def add_last(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = node

        self.size += 1

    def to_array(self):
        items = []
        last = self.head

        while last:
            items.append(last.data)
            last = last.next

        return items

    def remove(self, data):
        node_tbd = self.head

        if node_tbd:
            if node_tbd.data == data:
                self.head = node_tbd.next
                return

        while node_tbd:
            if node_tbd.data == data:
                prev.next = node_tbd.next
                return
            prev = node_tbd
            node_tbd = node_tbd.next

    def search(self, data):
        last = self.head

        while last:
            if last.data == data:
                return last
            last = last.next

        # Here we can also raise Exception("Element not found")
        return None


