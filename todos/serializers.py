from rest_framework import serializers
from .models import List, Todo, Detail


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = "__all__"


class TodoSerializer(serializers.ModelSerializer):
    details = DetailSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = "__all__"


class ListSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = "__all__"
