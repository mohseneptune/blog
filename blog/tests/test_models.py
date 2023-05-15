from django.test import TestCase
from blog.models import Category, Tag, Post
from django.contrib.auth import get_user_model
from django.utils.text import slugify


User = get_user_model()


class TestCategory(TestCase):
    def test_category_str(self):
        cat1 = Category.objects.create(name="cat #1")
        self.assertEqual(str(cat1), "cat #1")


class TestTag(TestCase):
    def test_tag_str(self):
        tag1 = Tag.objects.create(name="tag #1")
        self.assertEqual(str(tag1), "tag #1")


class TestPost(TestCase):
    def setUp(self):
        self.author = User.objects.create(username="admin", password="adminPwd")
        self.category = Category.objects.create(name="cat #1")
        self.post1 = Post.objects.create(
            title="post #1",
            content="some content about post 1",
            author=self.author,
            category=self.category,
        )

    def test_post_str(self):
        self.assertEqual(str(self.post1), "post #1")

    def test_post_slug(self):
        slugified_title = slugify(self.post1.title)

        post2 = Post.objects.create(
            title="post #1",
            content="some content about post 1",
            author=self.author,
            category=self.category,
        )

        self.assertEqual(self.post1.slug, slugified_title)
        self.assertNotEqual(self.post1.slug, post2.slug)
