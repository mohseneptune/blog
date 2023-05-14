from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


admin.site.site_header = "Blog Admin Protal"
admin.site.site_title = "Blog Admin Protal"
admin.site.index_title = "Welcome to Blog Admin Protal"