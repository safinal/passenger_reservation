from datetime import date
import math

from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .forms import TransactionForm
from .models import Trip, Transaction
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def train_reservation(request):
    if request.method == 'GET':
        context = {'trips': False}
        if request.GET.get('origin_city'):
            if request.GET.get('full_coupe'):
                tickets_condition = F('train__coupes_capacity')
            else:
                tickets_condition = 1
            if int(request.GET.get('coupes_capacity', 0)) != 0:
                coupes_capacity = (int(request.GET.get('coupes_capacity')),)
            else:
                coupes_capacity = (4, 6)
            if int(request.GET.get('train_quality', 0)) != 0:
                train_quality = (int(request.GET.get('train_quality')),)
            else:
                train_quality = (1, 2, 3, 4, 5)
            query = Trip.objects.filter(
                origin_railway__city=request.GET.get('origin_city'),
                destination_railway__city=request.GET.get('destination_city'),
                starting_date=request.GET.get('starting_date'),
                remain_tickets__gte=tickets_condition,
                price__gte=request.GET.get('price_from', 0),
                price__lte=request.GET.get('price_to', 1000),
                train__coupes_capacity__in=coupes_capacity,
                train__quality__in=train_quality
            )
            if query.count() > 0:
                context['trips'] = query
            context['count'] = query.count()
        return render(request=request, template_name='train/train.html', context=context)


@csrf_exempt
@login_required(login_url='/login/')
def get_ticket(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    if request.method == 'GET':
        return render(request=request, template_name='train/get_ticket.html', context={'trip': trip, 'flag': False})
    elif request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid() and trip.starting_date >= date.today():
            tickets_number = form.cleaned_data.get('tickets_number')
            if tickets_number <= trip.remain_tickets:
                first_ticket_id = trip.train.total_capacity - trip.remain_tickets + 1
                last_ticket_id = first_ticket_id + tickets_number - 1
                ticket_id_list = list(range(first_ticket_id, last_ticket_id + 1))
                first_coupe_id = math.ceil(first_ticket_id / trip.train.coupes_capacity)
                last_coupe_id = math.ceil(last_ticket_id / trip.train.coupes_capacity)
                coupe_id_list = list(range(first_coupe_id, last_coupe_id + 1))

                tracking_code = form.cleaned_data.get('tracking_code')
                Transaction.objects.create(user=request.user, trip=trip, tracking_code=tracking_code)
                trip.users.add(request.user)
                trip.remain_tickets -= tickets_number
                trip.save()

                context = {'ticket_id_list': ticket_id_list, 'coupe_id_list': coupe_id_list}
                return render(request=request, template_name='train/bought_ticket.html', context=context)
        return render(request, 'train/get_ticket.html', {'trip': trip, 'flag': f'{form.errors}'})


@login_required(login_url='/login/')
def my_trips(request):
    if request.method == 'GET':
        trips = request.user.trip_set.all()
        return render(request, 'train/my_trips.html', {'trips': trips, 'count': trips.count()})
