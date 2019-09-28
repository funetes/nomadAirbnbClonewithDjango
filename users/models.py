from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENG = "English"
    LANGUAGE_KOR = "Korean"
    LANGUAGE_CHOICES = ((LANGUAGE_ENG, "Eng"), (LANGUAGE_KOR, "Kor"))
    CURRENCY_ENG = "USD"
    CURRENCY_KOR = "KRW"

    CURRENCY_CHOICES = ((CURRENCY_ENG, "Usd"), (CURRENCY_KOR, "Krw"))

    bio = models.TextField(default="", blank=True)
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        max_length=10, null=True, choices=GENDER_CHOICES, blank=True
    )
    birthDate = models.DateField(null=True, blank=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, null=True, max_length=3, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, null=True, max_length=3, blank=True
    )
    superHost = models.BooleanField(default=False)

