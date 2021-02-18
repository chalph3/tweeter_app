# tweets/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Tweet

class TweetTests(TestCase):
    ...

    def test_tweet_create_view(self):
        self.client.force_login(self.user) # new
        response = self.client.post(reverse('tweet_new'),
            {'body': 'New tweet'}, follow=True) # updated
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New tweet')