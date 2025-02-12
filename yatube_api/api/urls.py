from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/posts/<int:post_id>/comments/',
         CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('v1/posts/<int:post_id>/comments/<int:comment_id>/',
         CommentViewSet.as_view(
             {'get': 'retrieve', 'put': 'update',
              'patch': 'partial_update', 'delete': 'destroy'})),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
