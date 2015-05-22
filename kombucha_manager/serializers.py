from django.contrib.auth.models import User, Group
from rest_framework import serializers

from kombucha_manager.models import *


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    #users = UserSerializer(source='user_profiles.user', many=True)

    class Meta:
        model = Organization
        fields = ('url',
                  'name',
                  'vessels',
                  #'users'
                 )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    #organization = OrganizationSerializer(source='user_profile.organization')

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name')
        lookup_field = 'username'


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    #user = serializers.Field(source='user.username')

    class Meta:
        model = UserProfile
        #fields = ('user')

class VesselSerializer(serializers.HyperlinkedModelSerializer):
    #organization = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all())
    #current_batch = serializers.HyperlinkedRelatedField(read_only=True, view_name='batch-view', many=True)

    class Meta:
        model = Vessel
        fields = ('id', 'url', 'name', 'batches')

    

class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = ('id', 'name', 'source_url', 'url')

class TeaTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeaType
        fields = ('id', 'name', 'url')

class TeaSerializer(serializers.HyperlinkedModelSerializer):
    types = TeaTypeSerializer(source='tea_types', many=True)
    sources = SourceSerializer(many=True)

    class Meta:
        model = Tea
        fields = ('id', 'url', 'name', 'comments', 'types', 'sources')

class BatchSerializer(serializers.HyperlinkedModelSerializer):
    teas = TeaSerializer(source='tea', many=True)
    vessel = VesselSerializer()

    class Meta:
        model = Batch
        fields = ('id',
                  'teas',
                  'tea_volume',
                  'sugar_volume',
                  'brew_volume',
                  'scoby_count',
                  'brew_date',
                  'comments',
                  'vessel',
                 )
    

class FlavorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flavor

class BottleSizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BottleSize

class BottleSerializer(serializers.HyperlinkedModelSerializer):
    size = BottleSizeSerializer()

    class Meta:
        model = Bottle
        fields = ('id',
                  'url',
                  'size',
                  'flavors',
                  'bottle_date',
                  'comments',
                  'batch',
                  )
