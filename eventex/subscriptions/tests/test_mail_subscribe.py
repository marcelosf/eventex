from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Marcelo Schneider', cpf='1234567890', 
                email='marcelo@gmail.com', phone='11-98888-8888')
        self.response = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'marcelo@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):

        contents = [
            'Marcelo',
            '1234567890',
            'marcelo@gmail.com',
            '11-98888-8888'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)