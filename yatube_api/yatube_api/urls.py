from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView)
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, GroupViewSet, FollowViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/posts/<int:post_id>/comments/',
         CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='comments'),
    path('api/v1/posts/<int:post_id>/comments/<int:pk>/',
         CommentViewSet.as_view({'get': 'retrieve',
                                'put': 'update', 'patch': 'partial_update',
                                 'delete': 'destroy'}),
         name='comment-detail'),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    path(
        'api/v1/jwt/create/',
        TokenObtainPairView.as_view(), name='jwt-create'),
    path(
        'api/v1/jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('api/v1/jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
]
