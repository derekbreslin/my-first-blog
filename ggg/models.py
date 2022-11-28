from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Entryggg(models.Model):
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    season = models.IntegerField()
    seasonround = models.IntegerField()
    tournamentweek = models.IntegerField()
    gameone = models.IntegerField()
    gametwo = models.IntegerField()
    gamethree = models.IntegerField()
    gamefour = models.IntegerField()
    gamefive = models.IntegerField()
    gwpoints = models.IntegerField()
    gwspeedscore = models.IntegerField()
    totalpoints = models.IntegerField()
    totalspeedscore = models.IntegerField()
    position = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.player

    def publish(self):
        self.save()
        