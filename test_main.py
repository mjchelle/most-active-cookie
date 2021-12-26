from unittest import TestCase
# import unittest
import main as mainClass


class TestCookies(TestCase):
    cookie = mainClass.Cookies()
    arr = [["cook", "2018-12-09T14:19:00+00:00"], ["cookie", "2018-12-09T10:13:00+00:00"],
           ["oreo", "2018-12-09T07:25:00+00:00"], ["chips", "2018-12-08T22:03:00+00:00"],
           ["cake", "2018-12-08T21:30:00+00:00"], ["cream", "2018-12-07T23:30:00+00:00"],
           ["cook", "2018-12-05T14:19:00+00:00"]]

    def test_first(self):
        self.assertEqual(0, self.cookie.first(self.arr, 0, len(self.arr) - 1, "2018-12-09",
                                              len(self.arr)))
        self.assertEqual(3, self.cookie.first(self.arr, 0, len(self.arr) - 1, "2018-12-08",
                                              len(self.arr)))
        self.assertEqual(5, self.cookie.first(self.arr, 0, len(self.arr) - 1, "2018-12-07",
                                              len(self.arr)))
        self.assertEqual(-1, self.cookie.first(self.arr, 0, len(self.arr) - 1, "2018-12-06",
                                               len(self.arr)))

    def test_last(self):
        self.assertEqual(2, self.cookie.last(self.arr, 0, len(self.arr) - 1, "2018-12-09",
                                             len(self.arr)))
        self.assertEqual(4, self.cookie.last(self.arr, 0, len(self.arr) - 1, "2018-12-08",
                                             len(self.arr)))
        self.assertEqual(5, self.cookie.last(self.arr, 0, len(self.arr) - 1, "2018-12-07",
                                             len(self.arr)))
        self.assertEqual(-1, self.cookie.last(self.arr, 0, len(self.arr) - 1, "2018-12-06",
                                              len(self.arr)))

    def test_find_most_active(self):
        self.assertEqual(["cook", "cookie", "oreo"], self.cookie.find_most_active
        (self.arr, 0, 2))
        self.assertEqual(["chips", "cake"], self.cookie.find_most_active
        (self.arr, 3, 4))
        self.assertEqual(["cream"], self.cookie.find_most_active
        (self.arr, 5, 5))
        self.assertEqual(["cook"], self.cookie.find_most_active
        (self.arr, 0, 6))
