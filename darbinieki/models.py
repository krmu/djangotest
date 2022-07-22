from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model()

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password):
        """
        Creates and saves a staff user with the given username and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    objects = UserManager()
    username = models.CharField(
        verbose_name='Lietotājvārds',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True,verbose_name="Aktīvs")
    staff = models.BooleanField(default=False,verbose_name="Ir darbinieks") # a admin user; non super-user
    admin = models.BooleanField(default=False,verbose_name="Ir administrators") # a superuser
    vards = models.CharField(max_length=255,default='-',verbose_name="Vārds") # a superuser
    uzvards = models.CharField(max_length=255,default='-',verbose_name="Uzvārds") # a superuser

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['vards','uzvards'] # username &amp; Password are required by default.

    def get_full_name(self):
        # The user is identified by their username address
        return self.vards + " "+ self.uzvards

    def get_short_name(self):
        # The user is identified by their username address
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin