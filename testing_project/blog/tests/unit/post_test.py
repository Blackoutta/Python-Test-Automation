from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test Content')
        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)

    def test_json(self):
        p = Post('Test_Title', 'Test_Content')
        expected = {
            "title": p.title,
            "content": p.content,
        }
        self.assertDictEqual(expected, p.json())
