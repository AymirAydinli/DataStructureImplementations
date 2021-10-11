import unittest
from hashmapcomplex import HashMapComplex


class TestHashMapComplex(unittest.TestCase):
    def test_hashmapcomplex(self):
        hashmapcomplex = HashMapComplex(200)

        self.assertEqual(hashmapcomplex._filled, 0, "_filled should return 0")
        hashmapcomplex.add(10, "Google")
        hashmapcomplex.add(10, "Amazon")
        hashmapcomplex.add("K", 10)
        hashmapcomplex.add("TMZ", "Uber")

        self.assertEqual(hashmapcomplex._filled, 4, "_filled should return 4")
        self.assertEqual(hashmapcomplex._size, 200, "_size should return 200")
        self.assertEqual(hashmapcomplex.get(10).value, "Google", "get function should return Google")
        self.assertEqual(hashmapcomplex.get(10).next.value, "Amazon", "get function should return Amazon")
        self.assertEqual(hashmapcomplex.get("K").value, 10, "get function should return int 10")

        self.assertEqual(hashmapcomplex.remove("K"), 10, "remove function should return 10 and remove value from array")
        self.assertEqual(hashmapcomplex._filled, 3, "_filled should return 3")
        self.assertEqual(hashmapcomplex.get("K"), None, "get function should return None")
        self.assertEqual(hashmapcomplex.remove(10), "Google", "remove function should return Google and remove value "
                                                              "from LinkedList")

        self.assertEqual(hashmapcomplex._filled, 2, "_filled should return 2")


if __name__ == "__main__":
    unittest.main()
