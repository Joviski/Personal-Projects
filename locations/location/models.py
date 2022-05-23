from django.db import models
from smart_selects.db_fields import ChainedForeignKey
# Create your models here.

class Continent(models.Model):
    continent= models.CharField(max_length=200)

    def __str__(self):
        return self.continent

class Country(models.Model):
    continent= models.ForeignKey(Continent, on_delete=models.CASCADE)
    country= models.CharField(max_length=200)
    def __str__(self):
        return self.country

class City(models.Model):
    country= models.ForeignKey(Country, on_delete=models.CASCADE)
    city_name=models.CharField(max_length=200)

    def __str__(self):
        return self.city_name

class Location(models.Model):
    continent= models.ForeignKey(Continent,on_delete=models.CASCADE)
    country= ChainedForeignKey(Country,
                               chained_field='continent',
                               chained_model_field='continent',
                               show_all=False,
                               auto_choose=True,
                               null=True,
                               blank=True)

    city= ChainedForeignKey(City,chained_field='country',
                               chained_model_field='country',
                               show_all=False,
                               auto_choose=True,
                               null=True,
                               blank=True)

    def __str__(self):
        return f'{self.country}, {self.city}'