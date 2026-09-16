from django.db import models

# Create your models here.
class Player(models.Model):
	username = models.CharField(max_length=255)
	avatar_url = models.URLField(max_length=255)
	score = models.IntegerField()

	def __str__(self):
		return self.name

class Match(models.Model):
	player1 = models.CharField(max_length=255)
	player2 = models.CharField(max_length=255)
	score_p1 = models.IntegerField()
	score_p2 = models.IntegerField()

	def __str__(self):
		return f"{self.player1} has faced {self.player2}"

