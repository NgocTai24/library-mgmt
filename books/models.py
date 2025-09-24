from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    published_year = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.title
