from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from user_contacts.models import Contact, Address


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    contacts = serializers.HyperlinkedRelatedField(many=True, queryset=Contact.objects.all(),
                                                   view_name='contact-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'contacts')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    addresses = serializers.HyperlinkedRelatedField(view_name='address-detail', many=True,
                                                    queryset=Address.objects.all())

    class Meta:
        model = Contact
        fields = ('phone', 'user', 'addresses')


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('name', 'city', 'address', 'contact')


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
