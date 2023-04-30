from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    
    def create_user(self, email, password, name, gender, age, introduction=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            gender=gender,
            age=age,
            introduction=introduction,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, name, gender, age, introduction=None):

        user = self.create_user(
            email,
            password=password,
            name=name,
            gender=gender,
            introduction=introduction,
            age=age,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    age = models.IntegerField(blank=True)
    name = models.CharField(max_length=50)
    introduction = models.TextField(default="Please enter the contents", blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    GENDER_CHOICES = [
        ('Male', '남성'),
        ('Female', '여성'),
    ]
    gender = models.CharField(
        max_length = 10,
        choices = GENDER_CHOICES
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name', 'gender', 'age', 'introduction']

    def __str__(self):
        return self.email

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
        # Simplest possible answer: All admins are staff
        return self.is_admin