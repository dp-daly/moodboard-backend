from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/artobjects/', include('artobjects.urls')),
    path('api/boards/', include('moodboards.urls')),
    path('api/auth/', include('jwt_auth.urls'))
]
