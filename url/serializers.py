from rest_framework import serializers
from url.models import URL


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['hash', 'url', 'created_at', 'visits']
