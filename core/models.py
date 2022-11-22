from django.db import models

class Hoodie(models.Model):
    typee = models.CharField(max_length=20)
    quality = models.TextField()
    price = models.IntegerField()
    picture = models.CharField(max_length=255)

    def __str__(self):
        return self.typee
    
    
class H0odie1(models.Model):
    typee = models.CharField(max_length=20)
    quality = models.TextField(max_length=700)
    price = models.FloatField(default=1)
    picture = models.CharField(max_length=255)
    
    def __str__(self):
        return self.typee

class Hoodie2(models.Model):
    typee = models.CharField(max_length=20)
    quality = models.TextField(max_length=700)
    price = models.FloatField(default=1)
    picture = models.CharField(max_length=255)
    
    def __str__(self):
        return self.typee

class Hoodie3(models.Model):
    typee = models.CharField(max_length=20)
    quality = models.TextField(max_length=20)
    price = models.FloatField(default=1)
    picture = models.CharField(max_length=255)
    
    def __str__(self):
        return self.typee

class Hoodie4(models.Model):
    typee = models.CharField(max_length=20)
    quality = models.CharField(max_length=20)
    price = models.FloatField(default=1)
    picture = models.CharField(max_length=255)
    
    def __str__(self):
        return self.typee    