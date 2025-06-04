from rest_framework import serializers

from backend.models import People


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'
