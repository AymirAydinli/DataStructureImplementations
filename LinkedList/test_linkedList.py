import unittest
from linkedList import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_linkedList(self):
        ll = LinkedList()

        self.assertEqual(ll.printList(), [], "linkedlist should be empty")

        ll.add_last(2)
        ll.add_last(3)
        ll.add_last(4)
        ll.add_first(1)

        self.assertEqual(ll.printList(),[1,2,3,4],"printList should return 1,2,3,4")
        self.assertEqual(ll.search(3),True,"search should return True")

        ll.remove(3)

        self.assertEqual(ll.search(3),False,"search should return False")
        self.assertEqual(ll.printList(),[1,2,4],"printList should return [1,2,4]")




if __name__ == "__main__":
    unittest.main()
