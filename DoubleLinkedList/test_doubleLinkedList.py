import unittest
from doubleLinkedList import DoubleLinkedList


class TestDoubleLinkedList(unittest.TestCase):
    def testDoubleLinkedList(self):
        ll = DoubleLinkedList()

        self.assertEqual(ll.to_array(), [], "linkedlist should be empty")

        ll.add_last(2)
        ll.add_last(4)
        ll.add_front(0)
        ll.add_after(2, 3)
        ll.add_before(2, 1)

        self.assertEqual(ll.size, 5, "Should return 5")
        self.assertEqual(ll.to_array(), [0, 1, 2, 3, 4], "to_array should return 0,1,2,3,4")
        self.assertEqual(ll.to_reverse_array(), [4, 3, 2, 1, 0], "to_reverse_array should return 4,3,2,1,0")
        self.assertTrue(ll.search(3))

        ll.remove(3)

        self.assertRaises(Exception, ll.search, 3)
        self.assertEqual(ll.to_array(), [0, 1, 2, 4], "printForward should return [0,1,2,4]")
        self.assertEqual(ll.to_reverse_array(), [4, 2, 1, 0], "printBackward should return [4,2,1,0]")
        self.assertEqual(ll.size, 4, "Should return 4")


if __name__ == "__main__":
    unittest.main()
