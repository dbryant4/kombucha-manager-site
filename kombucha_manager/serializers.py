from django.contrib.auth.models import User, Group
from rest_framework import serializers

from kombucha_manager.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    organization = serializers.CharField(source='user_profile.organization')

    class Meta:
        model = User
        fields = ('username', 'email', 'organization')
        lookup_field = 'username'


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.Field(source='user.username')

    class Meta:
        model = UserProfile
        fields = ('user')


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    #users = UserSerializer(source='user_profiles', many=True)

    class Meta:
        model = Organization
        fields = ('name',
                  'vessels',
                  #'users'
                 )


class BatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Batch
        fields = ('tea',
                  'tea_volume',
                  'sugar_volume',
                  'brew_volume',
                  'scoby_count',
                  'brew_date',
                  'comments',
                  'vessel',
                 )

class VesselSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vessel

class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source

class TeaTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeaType
        fields = ('name',)

class TeaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tea

class FlavorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flavor

class BottleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bottle
