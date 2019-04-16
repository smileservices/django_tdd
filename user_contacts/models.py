from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    phone = models.CharField(max_length=128)

    def __str__(self):
        return ", ".join(["%s %s" % (adr.name, adr.city) for adr in self.addresses.all()])


class Address(models.Model):
    city = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='addresses')

    def __str__(self):
        return "{} in {}".format(self.name, self.city)
