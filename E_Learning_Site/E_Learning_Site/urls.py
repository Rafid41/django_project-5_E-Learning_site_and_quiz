from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('App_Login.urls')),
    path('', include('App_Article.urls')),
    path('forum/', include('App_Forum.urls')),
    path('quiz/', include('App_Quiz.urls')),
]
