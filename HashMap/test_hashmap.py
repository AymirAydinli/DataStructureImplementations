import unittest
from hashmap import HashMap


class TestHashMap(unittest.TestCase):
    def test_hashmap(self):
        hashmap = HashMap(200)

        self.assertEqual(hashmap.capacity(), "length is: 200 and filled is: 0", "capacity should return the length and "
                                                                                "capacity of hashmap")

        hashmap.add(10, "Amazon")
        hashmap.add("Arthur", "Facebook")
        hashmap.add("a", "Google")
        hashmap.add(60, "Uber")

        self.assertEqual(hashmap.capacity(), "length is: 200 and filled is: 4", "capacity should return the length and "
                                                                                "capacity of hashmap")
        self.assertEqual(hashmap.get(10), "Amazon", "it should get Amazon")
        self.assertEqual(hashmap.get("Arthur"), "Facebook", "it should get Facebook")
        self.assertEqual(hashmap.get(60), "Uber", "it should get Uber")
        self.assertEqual(hashmap.get(140), "Empty", "it should get Empty")

        hashmap.remove(10)

        self.assertEqual(hashmap.capacity(), "length is: 200 and filled is: 3", "capacity should return the length and "
                                                                                "capacity of hashmap")

        self.assertEqual(hashmap.remove(10), "index is already empty", "index is already empty")
        self.assertEqual(hashmap.add(60, "Citi"), "Collision happened, please input a different index", "Collision happened, "
                                                                                                "please input a "
                                                                                                "different index")


if __name__ == "__main__":
    unittest.main()
