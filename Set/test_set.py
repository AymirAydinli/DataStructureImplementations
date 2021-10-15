import unittest
from set import Set


class TestSet(unittest.TestCase):
    def test_set(self):
        set = Set(50)

        self.assertEqual(set.size, 50, "size should return 50")
        self.assertEqual(set._filled, 0, "_filled should return 0")

        set.add(10)
        set.add(20)
        set.add(50)
        set.add("Google")

        set.__iter__()
        set.__str__()

        self.assertEqual(set.contains(10), True, "contains should return True")
        self.assertEqual(set.contains("Google"), True, "contains should return True")

        set.delete(50)

        self.assertEqual(set.contains(50), False, "contains should return False")


if __name__ == "__main__":
    unittest.main()
