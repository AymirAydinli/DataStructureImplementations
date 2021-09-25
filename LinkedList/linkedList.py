class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# node = Node()

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        node = Node(data)
        node.next = self.head
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

    def printList(self):
        items=[]
        last = self.head
        while last is not None:
            #print(last.data)
            items.append(last.data)
            last = last.next
        return items

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
            prev = nodeH
            nodeH = nodeH.next

        prev.next = nodeH.next
        nodeH = None

    def search(self, data):
        last = self.head
        while last is not None:
            if last.data == data:
                return True
                break
            last = last.next
        return False

