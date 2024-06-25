from django.contrib import admin
from django.urls import path

urlpatterns = []
urlpatterns += [
    path("admin/", admin.site.urls),
]
