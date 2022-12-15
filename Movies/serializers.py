from rest_framework import serializers

from .models import Move,Drama,Action,Animation

class MovesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Move
        # fields=['id','name', 'owner', 'description'] # see specific field 
        fields=['Genre','updated_at']

class DramaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Drama
        # fields=['id','name', 'owner', 'description'] # see specific field 
        fields='__all__'

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Action
        # fields=['id','name', 'owner', 'description'] # see specific field 
        fields='__all__'

class AnimationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Animation
        # fields=['id','name', 'owner', 'description'] # see specific field 
        fields='__all__'