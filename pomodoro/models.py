from django.db import models
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField() 

    def __str__(self):
        return self.title

class business_profile(models.Model):
    business_name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
        
class contact(models.Model):
    owner = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    number = models.IntegerField()

class address(models.Model):
    street = models.CharField(max_length=100)
    block = models.CharField(max_length=100)

class local_support(models.Model):
    rating = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)

class categories(models.Model):
    category = models.CharField(max_length=100)
    businesstype = models.CharField(max_length=100)

