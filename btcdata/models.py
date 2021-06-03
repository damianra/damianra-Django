from django.db import models

# Create your models here.
class BtcData(models.Model):
    date = models.CharField(max_length=20, primary_key=True)
    price = models.FloatField()
    var = models.FloatField()