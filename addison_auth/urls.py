from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("token_service.api.urls")),
]

admin.site.site_header = "Addison Auth Admin"