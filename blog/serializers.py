from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SlugRelatedField,
)

from blog.models import Category, Post, Tag


class CategorySerializer(ModelSerializer):
    posts = SlugRelatedField(many=True, slug_field='slug', read_only=True)

    class Meta:
        model = Category
        fields = ("name", "slug", "parent_category", "posts")

        extra_kwargs = {
            "slug": {"read_only": True},
        }


class TagSerializer(ModelSerializer):
    posts = SlugRelatedField(many=True, slug_field='slug', read_only=True)
    tag_detail = HyperlinkedIdentityField(
        view_name="tag-detail", lookup_field="slug", read_only=True
    )

    class Meta:
        model = Tag
        fields = "__all__"


class PostSerializer(ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"
