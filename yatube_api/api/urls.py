from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView)

from .views import PostViewSet, GroupViewSet, FollowViewSet, CommentViewSet


v1_router = DefaultRouter()
v1_router.register(r'posts', PostViewSet, basename='posts')
v1_router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = [

    path('v1/', include(v1_router.urls)),
    path('v1/follow/',
         FollowViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='follow'),
    path('v1/posts/<int:post_id>/comments/',
         CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='comments'),
    path('v1/posts/<int:post_id>/comments/<int:pk>/',
         CommentViewSet.as_view({'get': 'retrieve',
                                'put': 'update', 'patch': 'partial_update',
                                 'delete': 'destroy'}),
         name='comment-detail'),
    path('v1/jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('v1/jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('v1/jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),

]
