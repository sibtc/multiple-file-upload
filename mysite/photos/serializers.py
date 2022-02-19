from rest_framework import serializers
from .models import PhotoModel

class PhotoSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)

    class Meta:
        model = PhotoModel
        fields = (
            'title', 'file', 'uploaded_at'
        )
