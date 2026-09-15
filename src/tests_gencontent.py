import unittest

from gencontent import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        result = extract_title("# Hello")
        self.assertEqual(result, "Hello")

    def test_extract_title_no_h1(self):
        self.assertRaises(Exception, extract_title, "no heading here")


if __name__ == "__main__":
    unittest.main()