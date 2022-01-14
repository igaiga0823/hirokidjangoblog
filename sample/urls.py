from django.conf import settings #add
from django.contrib import admin
from django.urls import path, include #add
from django.conf.urls.static import static #add
 
urlpatterns = [
path('admin/', admin.site.urls),
path('', include('blog.urls')), # add
]
 
# 開発環境でのメディアファイルの配信設定 add
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
