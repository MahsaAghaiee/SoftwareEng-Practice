import unittest
from main import remove_duplicates, concat_strings

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates_basic(self):
        result = remove_duplicates("hello")
        self.assertEqual(result, "helo")

    def test_remove_duplicates_empty_str(self):
        result = remove_duplicates("")
        self.assertEqual(result, "")

    def test_remove_duplicates_none_str(self):
        result = remove_duplicates(None)
        self.assertEqual(result, None)

    def test_remove_duplicates_special_chars(self):
        result = remove_duplicates("!@#hello$%^")
        self.assertEqual(result, "!@#helo$%^")

class TestConcatStrings(unittest.TestCase):

    def test_concat_strings_basic(self):
        result = concat_strings("hello", "world")
        self.assertEqual(result, "helloworld")

    def test_concat_strings_empty_str(self):
        result = concat_strings("", "world")
        self.assertEqual(result, "world")

    def test_concat_strings_none_str(self):
        result = concat_strings(None, "world")
        self.assertEqual(result, "world")

    def test_concat_strings_ints(self):
        result = concat_strings("hello", str(123))
        self.assertEqual(result, "hello123")

if __name__ == '__main__':
    unittest.main()
