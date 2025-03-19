from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('', include('home_app.urls')),
    path('',include('account.urls')),
    path('article/',include('blog_app.urls')),
    path('admin/', admin.site.urls)
    
] 
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

