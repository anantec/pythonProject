from django.db import models

# Admin access model
class Access(models.Model):
    email = models.EmailField()
    password = models.TextField()

# User data model
class Users(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    age = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.name
