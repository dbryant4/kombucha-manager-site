from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from kombucha_manager.serializers import *
from kombucha_manager.models import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class VesselViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows vessels to be viewed or edited.
    """
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer

class BatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows batches to be viewed or edited.
    """
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer


class SourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sources to be viewed or edited.
    """
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class TeaTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tea types to be viewed or edited.
    """
    queryset = TeaType.objects.all()
    serializer_class = TeaTypeSerializer


class TeaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teas to be viewed or edited.
    """
    queryset = Tea.objects.all()
    serializer_class = TeaSerializer


class FlavorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows flavors to be viewed or edited.
    """
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer


class BottleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bottles to be viewed or edited.
    """
    queryset = Bottle.objects.all()
    serializer_class = BottleSerializer
