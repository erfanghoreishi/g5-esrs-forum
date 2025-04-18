import factory
from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model

class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()
    
    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'defaultpassword')
