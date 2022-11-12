from rest_framework import routers

from django.urls import include, path

from .views import GroupViewSet, PostViewSet, FollowViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register('groups', GroupViewSet, basename='groups')
router.register('posts', PostViewSet, basename='posts')
router.register('follow', FollowViewSet, basename='follow')
router.register(
    r'posts/(?P<post_id>[\d]+)/comments',
    CommentViewSet,
    basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include('djoser.urls')),
]
