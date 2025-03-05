from django.contrib import admin
from django.urls import path
from .views import welcome_view  # new

urlpatterns = [
    path("admin/", admin.site.urls),
    path("welcome/", welcome_view, name="welcome"),  # new
]
