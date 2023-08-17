from rest_framework import serializers
from .models import Profile

owner_username = serializers.ReadOnlyField(source="owner.username")
is_owner = serializers.SerializerMethodField()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'belt_level'
        ]
