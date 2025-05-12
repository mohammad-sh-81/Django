from .models import Event
from rest_framework import serializers
from django.contrib.auth import get_user_model


class TodoSerializer(serializers.ModelSerializer):

    def validate(self, max_attendees):
        max_attendees_specificat = 10
        if max_attendees_specificat < max_attendees:
            raise serializers.ValidationError('max_attendees_specificat is 10')

        return max_attendees


    class Meta:
        model = Event
        fields = '__all__'
