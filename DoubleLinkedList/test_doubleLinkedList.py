import unittest
from doubleLinkedList import DoubleLinkedList


class TestDoubleLinkedList(unittest.TestCase):
    def testDoubleLinkedList(self):
        ll = DoubleLinkedList()

        self.assertEqual(ll.printForward(), [], "linkedlist should be empty")

        ll.add_last(2)
        ll.add_last(4)
        ll.add_front(0)
        ll.add_after(2, 3)
        ll.add_before(2, 1)

        self.assertEqual(ll.printForward(), [0, 1, 2, 3, 4], "printForward should return 0,1,2,3,4")
        self.assertEqual(ll.printBackward(), [4, 3, 2, 1, 0], "printBackward should return 4,3,2,1,0")
        self.assertEqual(ll.search(3), True, "search should return True")

        ll.remove(3)

        self.assertEqual(ll.search(3), False, "search should return False")
        self.assertEqual(ll.printForward(), [0, 1, 2, 4], "printForward should return [0,1,2,4]")
        self.assertEqual(ll.printBackward(), [4, 2, 1, 0], "printBackward should return [4,2,1,0]")


if __name__ == "__main__":
    unittest.main()
