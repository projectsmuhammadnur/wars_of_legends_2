from django.db import models


class DonatStatusChoice(models.TextChoices):
    NEW = ('new', "New")
    CORRECT = ('correct', "Correct")
    INCORRECT = ('incorrect', "Incorrect")
