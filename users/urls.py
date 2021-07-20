from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users import views

urlpatterns = [
    path(
        'v1/auth/token/',
        views.EmailCodeTokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'v1/auth/token/refresh',
        views.EmailCodeTokenObtainPairView.as_view(),
        name='token_refresh'
    ),
    path(
        'v1/auth/email/',
        views.send_confirmation_code,
        name='send_confirmation_code'
    )
]

router_v1 = DefaultRouter()
router_v1.register('users', views.UsersViewSet, basename='users')

urlpatterns += [
    path('v1/', include(router_v1.urls)),
]
