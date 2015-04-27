from django.contrib.auth.models import User, Group
from rest_framework import serializers

from kombucha_manager.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class BatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Batch
        fields = ('tea',
                  'tea_volume',
                  'sugar_volume',
                  'brew_volume',
                  'scoby_count',
                  'brew_date',
                  'comments'
                 )


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
