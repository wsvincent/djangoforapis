from django.contrib import admin
from django.urls import path, include  # new


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("posts.urls")),  # new
]
