from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from .models import Post
from .serializers import PostSerializer


class PostListView(ListCreateAPIView):
    queryset = Post.published_objects.all()
    serializer_class = PostSerializer


class PostDetailView(RetrieveDestroyAPIView):
    queryset = Post.published_objects.all()
    serializer_class = PostSerializer
