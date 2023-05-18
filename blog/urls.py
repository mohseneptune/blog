from django.urls import path
from rest_framework.routers import SimpleRouter

from blog.views import CategoryViewSet, PostViewSet, TagViewSet

router = SimpleRouter()
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"tags", TagViewSet, basename="tag")
router.register(r"posts", PostViewSet, basename="post")

urlpatterns = router.urls
