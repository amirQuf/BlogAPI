from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Post, Category


class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Test Category', slug= "test", user = self.user  )
        self.post = Post.objects.create(
            title='Test Post',
            thumbnail='path/to/thumbnail.jpg',
            description='Test description',
            slug='test-post',
            user=self.user,
            voice='path/to/voice.wav',
            status='D'
        )
        self.post.categories.add(self.category)

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.user, self.user)
        self.assertEqual(self.post.categories.count(), 1)
        self.assertEqual(self.post.status, 'D')

    def test_get_absolute_url(self):
        expected_url = f"/{self.user.username}/{self.post.slug}"
        self.assertEqual(self.post.get_absolute_url(), expected_url)

    def test_ordering(self):
        # Create another post with a later created date
        later_post = Post.objects.create(
            title='Later Post',
            thumbnail='path/to/thumbnail.jpg',
            description='Later post description',
            slug='later-post',
            user=self.user,
            voice='path/to/voice.wav',
            status='D'
        )

        # Check that the later post comes before the earlier post
        self.assertGreater(later_post.created, self.post.created)
        self.assertEqual(
            list(Post.objects.all()),  # Retrieve all posts ordered by default ordering
            [later_post, self.post]  # Expected order
        )
