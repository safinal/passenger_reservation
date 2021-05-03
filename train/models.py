from django.db import models
from .validators import validate_satisfaction_range
from .cities import CITY_CHOICES


class Company(models.Model):
    name = models.CharField(max_length=50)
    satisfaction = models.FloatField(default=0, validators=[validate_satisfaction_range])

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(choices=CITY_CHOICES, max_length=100)

    def __str__(self):
        return self.name


class Railway(models.Model):
    name = models.CharField(max_length=50)
    city = models.OneToOneField(to=City, on_delete=models.CASCADE)
    companies = models.ManyToManyField(to=Company)

    def __str__(self):
        return self.name


class Train(models.Model):
    STAR_CHOICES = (
        (1, 'One Star'),
        (2, 'Two Star'),
        (3, 'Three Star'),
        (4, 'Four Star'),
        (5, 'Five Star'),
    )
    CAPACITY_CHOICES = (
        (4, 'Four Beds'),
        (6, 'Six Beds'),
    )

    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    current_city = models.ForeignKey(to=City, on_delete=models.PROTECT)
    quality = models.PositiveSmallIntegerField(choices=STAR_CHOICES)
    coupes_capacity = models.PositiveSmallIntegerField(choices=CAPACITY_CHOICES)
    total_capacity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.id}'


class Trip(models.Model):
    train = models.ForeignKey(to=Train, on_delete=models.PROTECT)
    origin_city = models.CharField(choices=CITY_CHOICES, max_length=100)
    destination_city = models.CharField(choices=CITY_CHOICES, max_length=100)
    starting_date = models.DateField()
    starting_time = models.TimeField()

    def __str__(self):
        return f'{self.id} {self.origin_city} - {self.destination_city}'
