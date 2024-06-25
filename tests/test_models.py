from django.test import TestCase, override_settings
from cache_cleaner.models import Cache


class CacheModelTest(TestCase):
    def setUp(self):
        self._cache_1 = Cache.objects.create(name="dummy_cache_1")
        self._cache_2 = Cache.objects.create(name="dummy_cache_2")

    def test_name_field(self):
        self.assertEqual(self._cache_1.name, "dummy_cache_1")
        self.assertEqual(self._cache_2.name, "dummy_cache_2")
        self.assertTrue(isinstance(self._cache_1, Cache))
        self.assertTrue(isinstance(self._cache_2, Cache))

    def test_str_method(self):
        self.assertEqual(str(self._cache_1), "dummy_cache_1")
        self.assertEqual(str(self._cache_2), "dummy_cache_2")

    @override_settings(CACHES={"project_cache_1": {}, "project_cache_2": {}})
    def test_update_from_settings(self):
        self.assertTrue(Cache.objects.filter(name="dummy_cache_1").exists())
        self.assertTrue(Cache.objects.filter(name="dummy_cache_2").exists())
        Cache.update_from_settings()
        self.assertFalse(Cache.objects.filter(name="dummy_cache_1").exists())
        self.assertFalse(Cache.objects.filter(name="dummy_cache_2").exists())
        self.assertTrue(Cache.objects.filter(name="project_cache_1").exists())
        self.assertTrue(Cache.objects.filter(name="project_cache_2").exists())
