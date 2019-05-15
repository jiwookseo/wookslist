from rest_framework import serializers
from .models import User
from todos.serializers import ListSerializer


class UserSerializer(serializers.ModelSerializer):
    lists = ListSerializer(many=True, read_only=True)
    # from_user = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'lists',
            # 'from_user',
        )
