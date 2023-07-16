from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()


class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
            role=User.MEMBER,
            profile=SimpleUploadedFile('test_profile.jpg', b'', content_type='image/jpeg')
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertEqual(self.user.role, User.MEMBER)
        self.assertEqual(str(self.user.profile), 'user/profile/test_profile.jpg')
        self.assertTrue(self.user.check_password('testpassword'))

    def test_user_str_representation(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_user_profile_upload_to(self):
        self.assertEqual(self.user._meta.get_field('profile').upload_to, 'user/profile/')
