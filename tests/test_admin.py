from unittest.mock import patch

from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase

from cache_cleaner.admin import CacheAdmin
from cache_cleaner.models import Cache


class CacheAdminTest(TestCase):
    def setUp(self):
        self._superuser = User.objects.create_superuser(
            "admin",
            "admin@example.com",
            "password",
        )
        self._client = Client()
        self._client.force_login(self._superuser)
        self._request = RequestFactory()
        self._url = "/admin/cache_cleaner/cache/"
        self._admin_site = AdminSite()
        self._cache_admin = CacheAdmin(Cache, self._admin_site)

    def test_get_queryset_calls_update_from_settings(self):
        with patch.object(Cache, "update_from_settings") as mock_update_from_settings:
            request = self._request.get(self._url)
            request.user = self._superuser
            self._cache_admin.get_queryset(request)
            mock_update_from_settings.assert_called_once()

    def test_has_add_permission(self):
        request = self._request.get(self._url)
        request.user = self._superuser
        self.assertFalse(self._cache_admin.has_add_permission(request))

    def test_has_change_permission(self):
        request = self._request.get(self._url)
        request.user = self._superuser
        self.assertFalse(self._cache_admin.has_change_permission(request))

    def test_has_delete_permission(self):
        request = self._request.get(self._url)
        request.user = self._superuser
        self.assertFalse(self._cache_admin.has_delete_permission(request))
