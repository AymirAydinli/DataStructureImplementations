import unittest
from hashmap import HashMap


class TestHashMap(unittest.TestCase):
    def test_hashmap(self):
        hashmap = HashMap(200)

        self.assertEqual(hashmap.capacity(), 200, "should return 200")

        hashmap.add(10, "Amazon")
        hashmap.add("Arthur", "Facebook")
        hashmap.add("a", "Google")
        hashmap.add(70, "Uber")

        self.assertEqual(hashmap.filled, 4, "Should return 4")
        self.assertEqual(hashmap.get(10), "Amazon", "should return Amazon")
        self.assertEqual(hashmap.get("Arthur"), "Facebook", "should return Facebook")
        self.assertEqual(hashmap.get(70), "Uber", "should get Uber")

        hashmap.remove(10)

        self.assertEqual(hashmap.filled, 3, "Should return 4")

        self.assertRaises(ValueError, hashmap.remove, 10)
        self.assertRaises(Exception, hashmap.get, 10)

        self.assertRaises(Exception, hashmap.add, 60)


if __name__ == "__main__":
    unittest.main()
