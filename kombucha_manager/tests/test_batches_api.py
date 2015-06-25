from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from django.utils import timezone

from django.contrib.auth.models import User
from ..models import *


class BatchesTestCase(APITestCase):
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

      user_profile = UserProfile(user=user, organization=self.organization)
      user_profile.save()

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

    def test_add_batch_using_api(self):
      """ Ensure we can add a batch using the API """

      url = reverse('batch-list')

      data = {
        'tea_volume': '12.0',
        'sugar_volume': '1.00',
        'brew_volume': '1.00',
        'scoby_count': 1,
        'brew_date': '2015-05-01',
        'comments': "",
        'tea': [reverse('tea-detail', kwargs={'pk': self.tea.id})],
        'vessel': reverse('vessel-detail', kwargs={'pk': self.vessel.id})
      }
      response = self.client.post(url, data, format='json')
      self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response)

    def test_patch_batch_using_api(self):
      """ Ensure we can patch a batch using the API """

      url = reverse('batch-detail', kwargs={'pk': self.batch.id})

      data = {
        'comments': 'This is a test comment for a batch'
      }
      response = self.client.patch(url, data, format='json')
      self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response)
      self.assertEqual(response.data['comments'], 'This is a test comment for a batch')

    def test_delete_batch_using_api(self):
      """ Ensure we can delete a batch using the API """

      url = reverse('batch-detail', kwargs={'pk': self.batch.id})

      response = self.client.delete(url, format='json')
      self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg=response.status_code)

    def test_getting_batch_using_api(self):
      """ Ensure we can get a batch using the API """

      url = reverse('batch-detail', kwargs={'pk': self.batch.id})

      response = self.client.get(url, format='json')
      self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.status_code)
      self.assertTrue(reverse('vessel-detail', kwargs={'pk': self.vessel.id}) in response.data['vessel'] , msg=response.content)

