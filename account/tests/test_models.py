from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class TestAccount(TestCase):
    def test_account_str(self):
        user = User.objects.create(username="admin", password="adminPwd")
        self.assertEqual(str(user), "admin")