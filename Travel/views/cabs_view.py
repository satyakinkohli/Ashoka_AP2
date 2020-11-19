from django.shortcuts import render
from django.views import View

from datetime import datetime, date
from Travel.models.cabs import Cab
from Travel.models.location import Location


class Cab_View(View):
    def get(self, request):
        cab_from = request.GET.get('cab_from')

        cab_to = request.GET.get('cab_to')

        cab_date = request.GET.get('cab_date')

        # converting date to required format
        now = date(*map(int, cab_date.split('-')))
        
        cab_min_time = datetime.min.time()
        cab_date_adjust = datetime.combine(now, cab_min_time)

        cab_date_formatted = datetime.strftime(cab_date_adjust, "%A; %d %b. %Y")

        cab_data = {'cab_from': cab_from, 'cab_to': cab_to, 'cab_date': cab_date_formatted}

        return render(request, 'cab_service_choice.html', cab_data)