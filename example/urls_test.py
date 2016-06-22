from django.conf.urls import include, url
from rest_framework import routers

from example.views import EntryViewSet, AuthorViewSet, EntryRelationshipView, \
    AuthorRelationshipView
from .api.resources.identity import Identity, GenericIdentity

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'polygons', EntryViewSet)
router.register(r'providers', AuthorViewSet)

# for the old tests
router.register(r'identities', Identity)

urlpatterns = [
    url(r'^', include(router.urls)),

    # old tests
    url(r'identities/default/(?P<pk>\d+)',
        GenericIdentity.as_view(), name='user-default'),

    url(r'^entries/(?P<pk>[^/.]+)/relationships/(?P<related_field>\w+)',
        EntryRelationshipView.as_view(),
        name='entry-relationships'),

    url(r'^authors/(?P<pk>[^/.]+)/relationships/(?P<related_field>\w+)',
        AuthorRelationshipView.as_view(),
        name='author-relationships'),
]

