from django.shortcuts import get_object_or_404

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import filters, permissions, status, viewsets
from rest_framework.throttling import ScopedRateThrottle

from posts.models import Group, Post, User
from .serializers import GroupSerializer, PostSerializer, CommentSerializer, FollowSerializer
from .permissions import IsAuthorOrReadOnlyPermission


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet группы."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet поста."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsAuthorOrReadOnlyPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet комментария."""
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsAuthorOrReadOnlyPermission]
    throttle_classes = ScopedRateThrottle
    # А далее применится лимит low_request
    # Для любых пользователей установим кастомный лимит 1 запрос в минуту
    throttle_scope = 'low_request' 

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
        return post








class FollowViewSet(viewsets.ModelViewSet):
    # http_method_names = ['get', 'post']
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'following__username']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        return user.follower


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)