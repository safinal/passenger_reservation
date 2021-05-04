from django.contrib import admin
from .models import Trip, Train, Railway, Company, Transaction

admin.site.register(Company)
admin.site.register(Railway)
admin.site.register(Train)
admin.site.register(Trip)
admin.site.register(Transaction)