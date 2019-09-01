from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SbscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Marcelo',
            cpf='12345678901',
            email='schneider.fei@gmail.com',
            phone='11-988888888'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)