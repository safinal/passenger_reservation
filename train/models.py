from datetime import date

from django.core.exceptions import ValidationError
from django.db import models
from .cities import CITY_CHOICES
from accounts.models import User


class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='train/images')

    def __str__(self):
        return self.name


class Railway(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(choices=CITY_CHOICES, max_length=100)
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
    current_railway = models.ForeignKey(to=Railway, on_delete=models.PROTECT)
    quality = models.PositiveSmallIntegerField(choices=STAR_CHOICES)
    coupes_capacity = models.PositiveSmallIntegerField(choices=CAPACITY_CHOICES)
    total_capacity = models.PositiveSmallIntegerField()

    def clean(self):
        if self.total_capacity % self.coupes_capacity != 0:
            raise ValidationError('Total capacity must be a coefficient of coupes capacity!')

    def __str__(self):
        return f'Train{self.id} - {self.company.name}'


class Trip(models.Model):
    origin_railway = models.ForeignKey(to=Railway, on_delete=models.CASCADE, related_name='origin_city')
    destination_railway = models.ForeignKey(to=Railway, on_delete=models.CASCADE, related_name='destination_city')
    train = models.ForeignKey(to=Train, on_delete=models.PROTECT)
    starting_date = models.DateField()
    starting_time = models.TimeField()
    remain_tickets = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()
    users = models.ManyToManyField(to=User, blank=True)

    def clean(self):
        if self.train.current_railway != self.origin_railway:
            raise ValidationError('This train is not available in the current railway!')
        if self.origin_railway == self.destination_railway:
            raise ValidationError("Origin and destination railways can't be the same!")
        if self.starting_date <= date.today():
            raise ValidationError("Starting date must be in the coming days!")
        if self.train.company not in self.origin_railway.companies.all() or self.train.company not in self.destination_railway.companies.all():
            raise ValidationError('Origin and destination railways both must have the train company')

    def __str__(self):
        return f'{self.id}_{self.origin_railway.city} - {self.destination_railway.city}'


class Transaction(models.Model):
    trip = models.ForeignKey(to=Trip, on_delete=models.PROTECT)
    user = models.ForeignKey(to=User, on_delete=models.PROTECT)
    date_time = models.DateTimeField(auto_now_add=True)
    tracking_code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.tracking_code
