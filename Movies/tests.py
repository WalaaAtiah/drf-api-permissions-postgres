from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import  status
# Create your tests here.
from django.contrib.auth import get_user_model
from .models import Drama,Move

from django.urls import reverse

class DramaTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass"
        )
        testuser2.save()

        testmove1=Move.objects.create(
            Genre='Drama'
        )
        testmove1.save()

        test_thing = Drama.objects.create(
            name="rake",
            publisher=testuser1,
            Genre=testmove1,
            global_assessment="8.1",
            duration="120"
        )
        test_thing.save()


    def setUp(self):
        self.client.login(username='testuser1', password="pass")




    def test_Drama_model(self):
        thing = Drama.objects.get(id=1)
        actual_publisher = str(thing.publisher)
        actual_name = str(thing.name)
        actual_duration = str(thing.duration)
        self.assertEqual(actual_publisher, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_duration, "120"
        )

    def test_get_Drama_list(self):
        url = reverse("Drama_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        things = response.data
        self.assertEqual(len(things), 1)
        

    def test_auth_required(self):
        self.client.logout()
        url = reverse("Drama_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_owner_can_delete(self):
        self.client.logout()
        self.client.login(username='testuser2', password="pass")
        url = reverse("Drama_detail", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)