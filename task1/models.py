from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=1, max_digits=10000)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=1, max_digits=5000)
    size = models.DecimalField(decimal_places=1, max_digits=1000)
    description = models.TextField()
    age_limited = models.BooleanField(False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)
