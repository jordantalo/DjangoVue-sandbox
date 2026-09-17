from django.db import models

# Create your models here.
class Player(models.Model):
	username = models.CharField(max_length=255, unique=True)
	avatar_url = models.URLField(max_length=255)
	score = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Match(models.Model):
	player1 = models.ForeignKey(
		Player,
		on_delete=models.SET_NULL,
		null=True,
		related_name="matches_as_p1"
		)
	player2 = models.ForeignKey(
		Player,
		on_delete=models.SET_NULL,
		null=True,
		related_name="matches_as_p2"
	)

	p1_username_snapshot = models.CharField(max_length=50, blank=True)
	p2_username_snapshot = models.CharField(max_length=50, blank=True)

	score_p1 = models.IntegerField(default=0)
	score_p2 = models.IntegerField(default=0)

	#created_at = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):

		if self.player1:
			self.p1_username_snapshot = self.player1.username

		if self.player2:
			self.p2_username_snapshot = self.player2.username

		super().save(*args, **kwargs)

