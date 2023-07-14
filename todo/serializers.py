from .models import Category, ToDo
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'created_at')


class ToDoSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    responsible_for_task = serializers.ReadOnlyField(source='responsible_for_task.username')
    category_id = serializers.ReadOnlyField(source='category.id')
    category_name = serializers.ReadOnlyField(source='category.title')

    class Meta:
        model = ToDo
        fields = '__all__'




