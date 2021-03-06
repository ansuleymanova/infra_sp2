from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('api/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('titles.urls')),
    path('api/', include('reviews.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
