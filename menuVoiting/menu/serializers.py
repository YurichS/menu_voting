from rest_framework import serializers
from .models import Menu


class MenuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class MenuUploadSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        menu = Menu(
            menu=validated_data['menu'],
            restaurant=validated_data['restaurant'],
        )

        menu.save()
        return menu

    class Meta:
        model = Menu
        fields = [
            'menu',
            'restaurant'
        ]

