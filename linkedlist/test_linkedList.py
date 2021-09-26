import unittest
from linkedList import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_linkedList(self):
        ll = LinkedList()

        self.assertEqual(ll.to_array(), [], "linkedlist should be empty")

        ll.add_last(2)
        ll.add_last(3)
        ll.add_last(4)
        ll.add_first(1)

        self.assertEqual(ll.to_array(), [1, 2, 3, 4], "to_array should return 1,2,3,4")

        node_3 = ll.search(3)
        self.assertIsNotNone(node_3, "search should not return None")
        self.assertEqual(node_3.data, 3, "search should return 3")

        ll.remove(3)

        self.assertEqual(ll.search(3), None, "search should return None")
        self.assertEqual(ll.to_array(), [1, 2, 4], "to_array should return [1,2,4]")


if __name__ == "__main__":
    unittest.main()
