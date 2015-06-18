
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from django.utils import timezone

from django.contrib.auth.models import User
from ..models import *


class BottlesTestCase(APITestCase):
    def setUp(self):
      username = 'admin'
      password = 'password'

      user = User(username=username, password=password)
      user.set_password(password)
      user.save()

      self.client = APIClient()
      self.client.login(username=username, password=password)

    def test_add_bottle_using_api(self):
      """ Ensure we can add a bottle using the API """

      organization = Organization(name='Test Organization Inc')
      organization.save()

      vessel = Vessel(name='test vessel', organization=organization)
      vessel.save()

      tea_type = TeaType(name='white')
      tea_type.save()

      source = Source(name='Neighborhood Test Market', source_url='')
      source.save()

      tea = Tea(comments='', name='Test Tea')
      tea.save()

      batch = Batch(vessel=vessel, tea_volume=1.0, sugar_volume=1.0, brew_volume=1.0, scoby_count=1, brew_date=timezone.now(), comments='')
      batch.save()

      size = BottleSize(size=1)
      size.save()

      flavor = Flavor(name='test flavor', comments='')
      flavor.save()

      url = reverse('bottle-list')

      data = {
      	'size': reverse('bottlesize-detail', kwargs={'pk': size.id}),
      	'bottle_date': '2015-05-01',
      	'comments': '',
      	'batch': reverse('batch-detail', kwargs={'pk': batch.id}),
        'flavors': [reverse('flavor-detail', kwargs={'pk': flavor.id})]
      }
      response = self.client.post(url, data, format='json')
      self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response)
