import unittest
from queue import Queue


class TestQueue(unittest.TestCase):

    def test_queue(self):
        queue = Queue()

        self.assertEqual(queue.size(), 0, "first size should be 0")

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)

        self.assertEqual(queue.size(), 4, "size should be 4")
        self.assertEqual(queue.peek(), 1, "peek should be 1")
        self.assertEqual(queue.dequeue(), 1, "dequeue should be 1")
        self.assertEqual(queue.dequeue(), 2, "dequeue should be 2")
        self.assertEqual(queue.size(), 2, "size should be 2")
        self.assertEqual(queue.peek(), 3, "peek should be 3")
        self.assertEqual(queue.empty(), False, "empty should be False")
        self.assertEqual(queue.dequeue(), 3, "dequeue should be 3")
        self.assertEqual(queue.dequeue(), 4, "dequeue should be 4")
        self.assertEqual(queue.empty(), True, "empty should be True")


if __name__ == "__main__":
    unittest.main()
