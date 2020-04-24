from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30)


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()


class daily(models.Model):
    name = models.CharField(max_length=30)
    sick = models.PositiveIntegerField()


class avrage(models.Model):
    name = models.CharField(max_length=30)
    typ = models.PositiveIntegerField()

class manths(models.Model):
    name = models.CharField(max_length=30)
    count = models.PositiveIntegerField()

class week(models.Model):
    name = models.CharField(max_length=30)
    num = models.PositiveIntegerField()




