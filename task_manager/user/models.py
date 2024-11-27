from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
