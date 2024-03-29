from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title