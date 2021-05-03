from django.contrib import admin
from .models import Trip, Train, Railway, Company

admin.site.register(Company)
admin.site.register(Railway)
admin.site.register(Train)
admin.site.register(Trip)
