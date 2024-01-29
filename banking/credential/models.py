from django.db import models

# Create your models here.




class District(models.Model):
    district=models.CharField(max_length=255)
    def __str__(self):
        return '{}'.format(self.district)

class Branches(models.Model):
    dist = models.ForeignKey(District, on_delete=models.CASCADE)
    branch=models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
           return '{}'.format(self.branch)

class Country(models.Model):
    name = models.CharField(max_length=60,null=False)

    def __str__(self):
        return f'{self.name}'
class City(models.Model):
    name = models.CharField(max_length=60,null=False)
    country = models.ForeignKey(to="Country",on_delete=models.CASCADE,related_name="city_set")

    def __str__(self):
        return f'{self.name}'

class Account_type(models.Model):
    type=models.CharField(max_length=60,null=False)
    def __str__(self):
        return f'{self.type}'

class Materials(models.Model):
    material=models.CharField(max_length=60,null=False)
    def __str__(self):
        return f'{self.material}'
class Gender(models.Model):
    gender=models.CharField(max_length=60,null=False)
    def __str__(self):
        return f'{self.gender}'


class Aplication(models.Model):
   pass

class Form_data(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    birthday = models.DateTimeField(blank=True,null=True)
    age = models.IntegerField()
    phone_num = models.IntegerField()
    account_type = models.CharField(max_length=70)
    district = models.CharField(max_length=60)
    branch = models.CharField(max_length=60)
    gender = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    address = models.TextField()
    materials = models.TextField()

    def __str__(self):
        return f'{self.firstname}'






