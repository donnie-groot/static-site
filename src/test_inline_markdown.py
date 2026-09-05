import unittest

from inline_markdown import extract_markdown_images, extract_markdown_links


class test(unittest.TestCase):
        def test_extract_markdown_images(self):
            matches = extract_markdown_images(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
            self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

        def test_extract_markdown_links(self):
            matches = extract_markdown_links(
            "this is text with a [link](https://www.youtube.com)"
            )
            self.assertListEqual([("link", "https://www.youtube.com")], matches)

if __name__ == "__main__":
    unittest.main()