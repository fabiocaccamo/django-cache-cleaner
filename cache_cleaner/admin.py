from django.contrib import admin, messages
from django.core.cache import caches
from django.utils.translation import gettext_lazy as _

from cache_cleaner.models import Cache


@admin.action(description=_("Clear selected caches"))
def clear_caches(modeladmin, request, queryset):
    for cache_obj in queryset:
        cache_name = cache_obj.name
        cache = caches[cache_name]
        cache.clear()
    caches_names = [cache_obj.name for cache_obj in queryset]
    caches_names_str = ", ".join(caches_names)
    messages.success(request, _("Cleared caches:") + f" {caches_names_str}.")


@admin.register(Cache)
class CacheAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)
    actions = [clear_caches]
    show_full_result_count = False

    def get_queryset(self, request):
        Cache.update_from_settings()
        return super().get_queryset(request)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
