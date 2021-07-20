from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Comment, Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    title = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        fields = '__all__'
        model = Review

    def validate(self, validated_data):
        user = self.context.get('author')
        title_id = self.context.get('title_id')
        review = Review.objects.filter(title__id=title_id, author=user)
        if review.exists() and self.context.get('action') != 'partial_update':
            raise ValidationError(
                'Review with such title and author already exists'
            )
        return validated_data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    review = serializers.SlugRelatedField(
        read_only=True,
        slug_field='text'
    )

    class Meta:
        fields = '__all__'
        model = Comment
