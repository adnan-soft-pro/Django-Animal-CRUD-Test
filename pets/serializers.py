from pets.models import Pet
from rest_framework import serializers


class PetSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Pet
        fields = '__all__'
