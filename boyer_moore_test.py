import unittest

from solution import boyer_moore_search  # Замініть 'your_module' на реальне ім'я вашого модулю

class TestBoyerMooreSearch(unittest.TestCase):
    def test_empty_needle(self):
        haystack = "abcde"
        needle = ""
        result = boyer_moore_search(haystack, needle)
        self.assertEqual(result, [0, 1, 2, 3, 4, 5])

    def test_no_match(self):
        haystack = "abcdefgh"
        needle = "xyz"
        result = boyer_moore_search(haystack, needle)
        self.assertEqual(result, [])

    def test_multiple_matches(self):
        haystack = "abracadabra"
        needle = "abra"
        result = boyer_moore_search(haystack, needle)
        self.assertEqual(result, [0, 7])

    def test_partial_overlap(self):
        haystack = "aaaaaa"
        needle = "aaa"
        result = boyer_moore_search(haystack, needle)
        self.assertEqual(result, [0, 1, 2, 3])

if __name__ == "__main__":
    unittest.main()
