from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Post, Comment, Group, Follow


User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following',)

    def validate_following(self, value):
        user = self.context['request'].user

        if user == value:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!')

        if Follow.objects.filter(user=user, following=value).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на этого пользователя.')

        return value
