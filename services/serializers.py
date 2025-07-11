from rest_framework import serializers
from .models import Service, ServiceImage
from core.models import Category


class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = ['id', 'image']


class ServiceSerializer(serializers.ModelSerializer):
    images = ServiceImageSerializer(many=True, read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    provider_username = serializers.CharField(source='provider.username', read_only=True)

    class Meta:
        model = Service
        fields = [
            'id',
            'title',
            'description',
            'location',
            'price',
            'is_active',
            'category',
            'category_name',
            'provider',
            'provider_username',
            'images',
            'created_at'
        ]
        read_only_fields = ['provider', 'created_at']

class ServiceImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = ['id', 'image', 'service']
        read_only_fields = ['id']
