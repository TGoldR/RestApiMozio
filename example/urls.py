from django.conf.urls import include, url
from rest_framework import routers

from example.views import EntryViewSet, AuthorViewSet
router = routers.DefaultRouter(trailing_slash=False)

router.register(r'polygons', EntryViewSet)
router.register(r'providers', AuthorViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
