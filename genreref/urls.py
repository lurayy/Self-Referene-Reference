from django.contrib import admin
from django.urls import path, include
from .logics import GenreAPI
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', GenreAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
