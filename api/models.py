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
    Mobilenumber = models.CharField(max_length=15, default="0000000000")
    email = models.EmailField()

    def __str__(self):
        return self.name





class Record(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    mobileNo = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)  # This might be required
    weight = models.FloatField()
    age = models.IntegerField()

    def __str__(self):
        return self.name
