from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('test_title', 'test_author')
        self.assertEqual('test_title', b.title)
        self.assertEqual('test_author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog("Test", "Test Author")
        b2 = Blog("My Day", "Rolf")

        self.assertEqual('Test by Test Author (0 post)', b.__repr__())
        self.assertEqual('My Day by Rolf (0 post)', b2.__repr__())

    def test_repr_multiple_posts(self):
        b = Blog("Test", "Test Author")
        b.posts = ['test']
        self.assertEqual(b.__repr__(), "Test by Test Author (1 post)")

        b2 = Blog("Life in California", "Roy Goode")
        b2.posts = ["howdy" for word in range(5)]
        self.assertEqual(b2.__repr__(), "Life in California by Roy Goode (5 posts)")
