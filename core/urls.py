from django.contrib import admin
from django.urls import path, include
from blog.views import PostListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/blog/', include('blog.urls')),
]


admin.site.site_header = "Blog Admin Protal"
admin.site.site_title = "Blog Admin Protal"
admin.site.index_title = "Welcome to Blog Admin Protal"