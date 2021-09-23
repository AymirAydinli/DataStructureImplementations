import unittest
from queue import Queue


class TestQueue(unittest.TestCase):

    def test_queue(self):
        queue = Queue()

        self.assertEqual(queue.size(), 0, "first size should be 0")

        queue.add(1)
        queue.add(2)
        queue.add(3)
        queue.add(4)

        self.assertEqual(queue.size(), 4, "size should be 4")
        self.assertEqual(queue.peek(), 1, "peek should be 1")
        self.assertEqual(queue.remove(), 1, "remove should be 1")
        self.assertEqual(queue.remove(), 2, "remove should be 2")
        self.assertEqual(queue.size(), 2, "size should be 2")
        self.assertEqual(queue.peek(), 3, "peek should be 3")
        self.assertEqual(queue.isEmpty(), None, "isEmpty should be False")
        self.assertEqual(queue.remove(), 3, "remove should be 3")
        self.assertEqual(queue.remove(), 4, "remove should be 4")
        self.assertEqual(queue.isEmpty(), True, "isEmpty should be True")

if __name__ == "__main__":
    unittest.main()