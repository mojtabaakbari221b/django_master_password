from django.test import TestCase
from django.contrib.auth import get_user_model
User = get_user_model()

class TestMasterPasswordBackend(TestCase):
    def test_valid_username_for_login_without_USE_ADMIN_USERNAME_FROM_SETTINGS(self):
        pass

    def test_invalid_username_for_login_without_USE_ADMIN_USERNAME_FROM_SETTINGS(self):
        pass

    def test_valid_admin_for_login_with_USE_ADMIN_USERNAME_FROM_SETTINGS(self):
        pass

    def test_invalid_admin_for_login_with_USE_ADMIN_USERNAME_FROM_SETTINGS(self):
        pass