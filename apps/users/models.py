from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """
    Кастомная модель пользователя. Взамен дефолтному пользователю от Django.
    """
    pass