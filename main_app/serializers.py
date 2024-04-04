from rest_framework import serializers
from .models import TVshow, Viewing

class TVshowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVshow
        fields = '__all__'

class ViewingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewing
        fields = '__all__'
        read_only_fields = ('show',)