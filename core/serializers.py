from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'category', 'from', 'title', 'text', 'thedate')


PostSerializer._declared_fields["from"] = serializers.CharField(source="from_whom")
PostSerializer._declared_fields["id"] = serializers.CharField(source="post_id")

