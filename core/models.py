from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


# Create your models here.
class UserManager(BaseUserManager):
    # BaseUserManager.create_user()

    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
#     원래 create_user > _create_user 실행되는데,
#     username 안쓰려고 여기서 한꺼번에 구현했다
