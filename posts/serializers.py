from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "created_at"]
