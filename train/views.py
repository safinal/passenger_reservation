from django.db.models import F
from django.shortcuts import render
from .forms import TripForm
from .models import Trip


def train_reservation(request):
    if request.method == 'GET':
        context = {'form': TripForm(), 'trips': False}
        if request.GET.get('origin_city'):
            if request.GET.get('full_coupe'):
                query = Trip.objects.filter(
                    origin_city=request.GET.get('origin_city'),
                    destination_city=request.GET.get('destination_city'),
                    starting_date=request.GET.get('starting_date'),
                    train__total_capacity__gte=F('train__coupes_capacity')
                )
            else:
                query = Trip.objects.filter(
                    origin_city=request.GET.get('origin_city'),
                    destination_city=request.GET.get('destination_city'),
                    starting_date=request.GET.get('starting_date'),
                    train__total_capacity__gte=1
                )
            if query.count() > 0:
                context['trips'] = query
        return render(request=request, template_name='train_reservation.html', context=context)
