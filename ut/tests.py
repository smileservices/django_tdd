from django.test import TestCase, Client
from django.shortcuts import resolve_url
from user_contacts.models import Contact, Address, User
from user_contacts.views import *


class ViewTest(TestCase):
    fixtures = ['users', 'contacts']
    test_200_urls = [
        ('/', "/"),
        ('users-list', resolve_url("user-list")),
        ('contacts-list', resolve_url("contact-list")),
        ('addresses-list', resolve_url("address-list")),
        ("user-detail", resolve_url('user-detail', 1)),
        ("contact-detail pk: 2", resolve_url('contact-detail', 2)),
        ("address-detail pk: 1", resolve_url('address-detail', 1)),
    ]

    def setUp(self):
        self.client_stub = Client()

    def test_views_200(self):
        for test in self.test_200_urls:
            name, url = test
            with self.subTest(msg=name,url=url):
                response = self.client_stub.get(url)
                self.assertEquals(response.status_code, 200)
