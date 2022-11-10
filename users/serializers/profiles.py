#Django Serializers
from rest_framework import serializers
from django.conf import settings

#Models
from users.models import Profile

class ProfileModelSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta class."""
        model = Profile
        fields = (
            'picture',
            'biography',
        )