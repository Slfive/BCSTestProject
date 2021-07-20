from django.db import models

# Create your models here.
class Block(models.Model):
	height_block = models.CharField(max_length=250)
	hash_block = models.CharField(max_length=400)
	time_block = models.CharField(max_length=100)
	miner_adress = models.CharField(max_length=300)
	quantity = models.CharField(max_length = 300)

	def __srt__(self):
		return self.height_block