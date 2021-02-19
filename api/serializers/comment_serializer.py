from rest_framework import serializers

from api.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Comment
