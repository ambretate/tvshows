from rest_framework import serializers
from .models import TVshow

class TVshowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVshow
        fields = '__all__'