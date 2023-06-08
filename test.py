import unittest
from main import concat_strings

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
