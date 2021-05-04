from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Trip, Transaction
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
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
        return render(request=request, template_name='train.html', context=context)


@csrf_exempt
@login_required(login_url='/login/')
def get_ticket(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    if request.method == 'GET':
        return render(request=request, template_name='get_ticket.html', context={'trip': trip, 'flag': False})
    elif request.method == 'POST':
        tracking_code = request.POST.get('tracking_code', '')
        tickets_number = int(request.POST.get('tickets_number'))
        if 0 < len(tracking_code) <= 20 and tickets_number <= trip.remain_tickets:
            Transaction.objects.create(user=request.user, trip=trip, tracking_code=tracking_code)
            trip.remain_tickets -= 1
            trip.save()
            trip.users.add(request.user)
            return render(request, 'bought_ticket.html')
        return render(request=request, template_name='get_ticket.html', context={'trip': trip, 'flag': True})
