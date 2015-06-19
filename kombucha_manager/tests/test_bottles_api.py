
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

      self.organization = Organization(name='Test Organization Inc')
      self.organization.save()

      self.vessel = Vessel(name='test vessel', organization=self.organization)
      self.vessel.save()

      self.tea_type = TeaType(name='white')
      self.tea_type.save()

      self.source = Source(name='Neighborhood Test Market', source_url='')
      self.source.save()

      self.tea = Tea(comments='', name='Test Tea')
      self.tea.save()

      self.batch = Batch(
                          vessel=self.vessel,
                          tea_volume=1.0,
                          sugar_volume=1.0,
                          brew_volume=1.0,
                          scoby_count=1,
                          brew_date=timezone.now(), 
                          comments=''
                        )
      self.batch.save()

      self.size = BottleSize(size=1)
      self.size.save()

      self.flavor = Flavor(name='test flavor', comments='')
      self.flavor.save()

      self.bottle = Bottle(
                        batch=self.batch,
                        size=self.size,
                        bottle_date=timezone.now(),
                        comments=''
                      )
      self.bottle.save()

    def test_add_bottle_using_api(self):
      """ Ensure we can add a bottle using the API """

      url = reverse('bottle-list')

      data = {
      	'size': reverse('bottlesize-detail', kwargs={'pk': self.size.id}),
      	'bottle_date': '2015-05-01',
      	'comments': '',
      	'batch': reverse('batch-detail', kwargs={'pk': self.batch.id}),
        'flavors': [reverse('flavor-detail', kwargs={'pk': self.flavor.id})]
      }
      response = self.client.post(url, data, format='json')
      self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response)

    def test_patch_bottle_using_api(self):
      """ Ensure we can patch a bottle using the API """

      url = reverse('bottle-detail', kwargs={'pk': self.bottle.id})

      data = {
        'comments': 'This is a test comment'
      }
      response = self.client.patch(url, data, format='json')
      self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response)
      self.assertEqual(response.data['comments'], 'This is a test comment')

    def test_delete_bottle_using_api(self):
      """ Ensure we can delete a bottle using the API """

      url = reverse('bottle-detail', kwargs={'pk': self.bottle.id})

      response = self.client.delete(url, format='json')
      self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg=response.status_code)

    def test_getting_bottle_using_api(self):
      """ Ensure we can get a bottle using the API """

      url = reverse('bottle-detail', kwargs={'pk': self.bottle.id})

      response = self.client.get(url, format='json')
      self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.status_code)
      self.assertTrue(reverse('bottlesize-detail', kwargs={'pk': self.size.id}) in response.data['size'] , msg=response.content)

