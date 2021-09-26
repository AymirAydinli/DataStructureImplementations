import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def test_stack(self):
        stack = Stack()

        self.assertEqual(stack.size(), 0, "Size should be 0")

        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.size(), 3, "Size should be 3")
        self.assertEqual(stack.peek(), 3, "Peek should be 3")
        self.assertEqual(stack.pop(), 3, "Pop should be 3")
        self.assertEqual(stack.pop(), 2, "Pop should be 2")
        self.assertEqual(stack.size(), 1, "Size should be 1")
        self.assertEqual(stack.pop(), 1, "Pop should be 1")
        self.assertEqual(stack.size(), 0, "Size should be 0")


if __name__ == '__main__':
    unittest.main()
