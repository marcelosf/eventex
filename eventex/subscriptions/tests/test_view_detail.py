from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Marcelo', 
            cpf='12345678910',
            email='marcelo.test@gmail.com',
            phone='11988888888'
        )
        self.resp = self.client.get('/inscricao/{}/'.format(self.obj.pk))
     
    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        content = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)

        with self.subTest():
            for expect in content:
                self.assertContains(self.resp, expect)

class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get('/inscricao/0/')
        self.assertEqual(404, resp.status_code)