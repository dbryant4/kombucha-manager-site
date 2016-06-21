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
    #last_batch = serializers.HyperlinkedRelatedField(queryset=Batch.objects.last(), view_name='batch-detail')

    class Meta:
        model = Vessel
        fields = ('id', 'url', 'name', 'batches')
        extra_kwargs = {'id': {'read_only': False}}

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
        extra_kwargs = {'id': {'read_only': False}}

class BatchSerializer(serializers.HyperlinkedModelSerializer):
    tea = TeaSerializer(many=True)
    # tea = serializers.HyperlinkedIdentityField(many=True, view_name='track-list')
    vessel = VesselSerializer()

    def create(self, validated_data):
        teas_data = validated_data.pop('tea')
        vessel_data = validated_data.pop('vessel')

        vessel = Vessel.objects.get(id=vessel_data['id'])
        batch = Batch(
            vessel = vessel,
            tea_volume = validated_data['tea_volume'],
            sugar_volume = validated_data['sugar_volume'],
            brew_volume = validated_data['brew_volume'],
            scoby_count = validated_data['scoby_count'],
            brew_date=validated_data['brew_date']
        )
        batch.save()
        for tea_data in teas_data:
            tea = Tea.objects.get(id=tea_data['id'])
            batch.tea.add(tea)

        return batch

    class Meta:
        model = Batch
        fields = ('id',
                  'url',
                  'tea',
                  'tea_volume',
                  'sugar_volume',
                  'brew_volume',
                  'scoby_count',
                  'brew_date',
                  'comments',
                  'vessel',
                  'discarded'
                 )


class FlavorSerializer(serializers.HyperlinkedModelSerializer):
    source = SourceSerializer(many=True)

    class Meta:
        model = Flavor
        fields = ('id', 'name', 'source', 'comments')
        extra_kwargs = {'id': {'read_only': False}}

class BottleSizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BottleSize
        fields = ('id', 'size')
        extra_kwargs = {'id': {'read_only': False}}

class BottleSerializer(serializers.HyperlinkedModelSerializer):
    size = BottleSizeSerializer()
    flavors = FlavorSerializer(many=True)

    def create(self, validated_data):
        flavors_data = validated_data.pop('flavors')
        size_data = validated_data.pop('size')

        size = BottleSize.objects.get(id=size_data['id'])

        bottle = Bottle(
            size=size,
            bottle_date=validated_data['bottle_date'],
            comments="",
            batch=validated_data['batch']
        )
        bottle.save()

        for flavor_data in flavors_data:
            flavor = Flavor.objects.get(id=flavor_data['id'])
            flavor.bottles.add(bottle)

        return bottle

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
