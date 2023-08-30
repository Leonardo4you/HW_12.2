from unittest import TestCase

from utils import arrs

"""pytest"""


class TestArrs:
    def test_get(self):
        assert arrs.get([1, 2, 3], 1, "test") == 2
        assert arrs.get([], -1, "test") == "test"

    def test_slice(self):
        assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
        assert arrs.my_slice([1, 2, 3], 1) == [2, 3]

        assert isinstance(arrs.my_slice([], 1), list)
        assert arrs.my_slice([], 1) == []
        assert arrs.my_slice([1, 2, 3]) == [1, 2, 3]
        assert arrs.my_slice([1, 2, 3], 0, 5) == [1, 2, 3]
        assert arrs.my_slice([1, 2, 3], 2, 1) == []
        assert arrs.my_slice([1, 2, 3], -2) == [2, 3]
        assert arrs.my_slice([1, 2, 3], 0, -1) == [1, 2]



"""unitests"""


class ArsTestCase(TestCase):
    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], -1, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])

        self.assertIsInstance(arrs.my_slice([], 1), list)
        self.assertEqual(arrs.my_slice([], 1), [])
        self.assertEqual(arrs.my_slice([1, 2, 3]), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 0, 5), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 2, 1), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], -2), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 0, -1), [1, 2])
