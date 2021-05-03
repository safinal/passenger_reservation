from django.db.models import F
from django.shortcuts import render
from .models import Trip


def train_reservation(request):
    if request.method == 'GET':
        context = {'trips': False}
        if request.GET.get('origin_city'):
            if request.GET.get('full_coupe'):
                query = Trip.objects.filter(
                    origin_railway__city=request.GET.get('origin_city'),
                    destination_railway__city=request.GET.get('destination_city'),
                    starting_date=request.GET.get('starting_date'),
                    remain_tickets__gte=F('train__coupes_capacity')
                )
            else:
                query = Trip.objects.filter(
                    origin_railway__city=request.GET.get('origin_city'),
                    destination_railway__city=request.GET.get('destination_city'),
                    starting_date=request.GET.get('starting_date'),
                    remain_tickets__gte=1
                )
            if query.count() > 0:
                context['trips'] = query
        return render(request=request, template_name='train_reservation.html', context=context)
