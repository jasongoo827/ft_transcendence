from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    # 친구 필드를 시리얼라이즈할 때 사용자 이름만 포함
    friends = serializers.SlugRelatedField(
        slug_field='username',  # 친구 목록에 사용자 이름을 포함
        queryset=CustomUser.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'nickname', 'wins', 'losses', 'friends']

    def update(self, instance, validated_data):
        # 'friends' 필드 업데이트 시 처리
        friends_data = validated_data.pop('friends', [])
        instance = super().update(instance, validated_data)
        # 현재 친구 목록에서 제거된 사용자들을 삭제
        current_friends = set(instance.friends.all())
        new_friends = set(friends_data)
        for friend in current_friends - new_friends:
            instance.friends.remove(friend)
        # 새 친구 목록에 추가
        for friend in new_friends - current_friends:
            instance.friends.add(friend)
        return instance
