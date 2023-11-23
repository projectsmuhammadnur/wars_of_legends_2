from django.db import models


class HeroRoleChoice(models.TextChoices):
    MARKSMAN = ('marksman', "Marksman")
    MAGE = ('mage', "Mage")
    FIGHTER = ('fighter', "Fighter")
    TANK = ('tank', "Tank")
