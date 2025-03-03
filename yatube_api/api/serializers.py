from django.contrib.auth import get_user_model

from rest_framework import serializers

from posts.models import Post, Comment, Group, Follow


User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['id', 'author', 'text', 'pub_date', 'image', 'group']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'created', 'post']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'title', 'slug', 'description']


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ['user', 'following']
        read_only_fields = ['user']

    def validate_following(self, value):
        user = self.context['request'].user

        if user == value:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя!")

        if Follow.objects.filter(user=user, following=value).exists():
            raise serializers.ValidationError(
                "Вы уже подписаны на этого пользователя.")

        return value
