import unittest
from blog.content import Article


article = """---
title: foo bar title
categories: cat1, cat2, cat3
---

# Hey!
Hello world

---

Foo
"""


class TestContent(unittest.TestCase):

    def setUp(self):
        self.article = article

    def test_content(self):
        a = Article(self.article)

        self.assertEquals(a.title, "foo bar title")
        self.assertEquals(a.categories, ["cat1", "cat2", "cat3"])
        self.assertEquals(a.text, "<h1>Hey!</h1>\n<p>Hello world</p>\n<hr />\n<p>Foo</p>")
