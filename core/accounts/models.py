from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('user must have an email address!')
        email = self.normalize_email(email)
        user = self.model(email=email,name=name,**extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,name,password, **extra_fields):
        user = self.create_user(email,name,password,**extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length = 255 , unique=True)
    name = models.CharField(max_length=255)
    lastname= models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    birth_date = models.DateField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['name','lastname','address']

    def get_full_name(self):
        return self.name
    
    def __str__(self):
        return self.email