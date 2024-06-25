from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CacheCleanerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cache_cleaner"
    verbose_name = _("Cache Cleaner")
