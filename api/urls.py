from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .serializers.user import EmailAuthSerializer
from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, Review_IDViewSet)
from .views.user import UserViewSet, send_confirmation_code

v1_router = DefaultRouter()
v1_router.register(r'users', UserViewSet)
v1_router.register('categories', CategoryViewSet, basename='categories')
v1_router.register('genres', GenreViewSet, basename='genres')
v1_router.register('titles', TitleViewSet, basename='titles')
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)',
    Review_IDViewSet,
    basename='reviews_id'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments/(?P<comment_id>\d+)',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/auth/email/', send_confirmation_code),
    path(
        'v1/token/',
        TokenObtainPairView.as_view(serializer_class=EmailAuthSerializer),
        name='token_obtain_pair'
    ),
    path(
        'v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path('v1/', include(v1_router.urls)),
]
