from django_filters import CharFilter, FilterSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from blog.models import Category, Post, Tag
from blog.serializers import CategorySerializer, PostSerializer, TagSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class CategoryFilter(FilterSet):
    name = CharFilter(lookup_expr="icontains")


class TagFilter(FilterSet):
    name = CharFilter(lookup_expr="icontains")


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"
    filterset_class = CategoryFilter

    @action(detail=True)
    def posts(self, request, slug=None):
        posts = Post.objects.filter(category__slug=slug)
        serializer = PostSerializer(posts, many=True, context={"request": request})
        return Response(serializer.data, status=HTTP_200_OK)


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "slug"
    filterset_class = TagFilter

    @action(detail=True)
    def posts(self, request, slug=None):
        posts = Post.objects.filter(tags__slug=slug)
        serializer = PostSerializer(posts, many=True, context={"request": request})
        return Response(serializer.data, status=HTTP_200_OK)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"
