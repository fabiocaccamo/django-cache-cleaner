from django.conf import settings
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _


class Cache(models.Model):
    class Meta:
        ordering = ["name"]
        verbose_name = _("Cache")
        verbose_name_plural = _("Caches")

    @classmethod
    def update_from_settings(cls):
        manager = cls.objects
        settings_caches = set(settings.CACHES.keys())
        existing_caches = set(manager.values_list("name", flat=True))
        caches_to_create = settings_caches - existing_caches
        caches_to_delete = existing_caches - settings_caches

        with transaction.atomic():
            if caches_to_create:
                manager.bulk_create(
                    [Cache(name=cache_name) for cache_name in caches_to_create]
                )
            if caches_to_delete:
                manager.filter(name__in=caches_to_delete).delete()

    name = models.CharField(
        verbose_name=_("Name"),
        primary_key=True,
        max_length=255,
    )

    def __str__(self):
        return f"{self.name}"
