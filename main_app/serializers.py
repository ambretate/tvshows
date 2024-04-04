from rest_framework import serializers
from .models import TVshow, Viewing, Cast

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model: Cast
        fields = '__all__'

class TVshowSerializer(serializers.ModelSerializer):
    actors = CastSerializer(many=True, read_only=True)

    class Meta:
        model = TVshow
        fields = '__all__'

class ViewingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewing
        fields = '__all__'
        read_only_fields = ('show',)