from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """Must only accep digits"""
        form = self.make_validated_form(cpf='axd1234561')
        self.assertFromErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits"""
        form = self.make_validated_form(cpf='1234')
        self.assertFromErrorCode(form, 'cpf', 'length')

    def assertFromErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def assertFromErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Marcelo', cpf='12345678901', 
                email='marcelo@test.com', phone='11999999999')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)

        return form