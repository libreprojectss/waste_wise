#serializer to save image
from rest_framework import serializers
from images_processor.models import Images

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"
