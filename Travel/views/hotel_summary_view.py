from django.shortcuts import render
from django.views import View
from datetime import datetime
from Travel.models.hotels import Hotel
from Travel.models.hotel_booking import Hotel_booking
from Travel.models.flights import Flight

from datetime import datetime, date

import random

class Hotel_Summary_View(View):
    def get(self, request):
        hotel_id = request.GET.get('hotel_id')
        hotel_instance = Hotel.get_hotel_through_id(hotel_id)

        hotel_check_in = request.GET.get('hotel_check_in')
        hotel_check_out = request.GET.get('hotel_check_out')
        
        hotel_check_in_1 = datetime.strptime(hotel_check_in, '%Y-%m-%d')
        hotel_check_out_1 = datetime.strptime(hotel_check_out, '%Y-%m-%d')
        days = hotel_check_out_1 - hotel_check_in_1

        # converting date to required format
        now = date(*map(int, hotel_check_in.split('-')))

        hotel_min_time = datetime.min.time()
        hotel_check_in_adjust = datetime.combine(now, hotel_min_time)

        hotel_check_in_formatted = datetime.strftime(
        hotel_check_in_adjust, "%A; %d %b. %Y")
        # end conversion

        # converting date to required format
        now = date(*map(int, hotel_check_out.split('-')))

        hotel_min_time = datetime.min.time()
        hotel_check_out_adjust = datetime.combine(now, hotel_min_time)

        hotel_check_out_formatted = datetime.strftime(
        hotel_check_out_adjust, "%A; %d %b. %Y")
        # end conversion

        standard_number = request.GET.get('standard')
        # print(standard_number)
        deluxe_number = request.GET.get('deluxe')
        # print(deluxe_number)
        premium_number = request.GET.get('premium')
        # print(premium_number)
        suite_number = request.GET.get('suite')
        # print(suite_number)

        number_of_rooms = int(standard_number) + int(deluxe_number) + \
            int(premium_number) + int(suite_number)

        price_per_night = (int(standard_number)*float(hotel_instance.standard_price)) + (int(deluxe_number)*float(hotel_instance.deluxe_price)
                                                                                         ) + (int(premium_number)*float(hotel_instance.premium_price)) + (int(suite_number)*float(hotel_instance.suite_price))
        print(price_per_night)
        total_price = int(price_per_night)*int(days.days)
        print(total_price)

        user = request.user
        hotel_booking_instance = Hotel_booking(user_email=user.email,
                                               user_fname=user.first_name,
                                               user_lname=user.last_name,
                                               hotel=hotel_instance,
                                               check_in_date=hotel_check_in_1,
                                               check_out_date=hotel_check_out_1,
                                               total_price=total_price,
                                               standard_number=int(
                                                   standard_number),
                                               deluxe_number=int(
                                                   deluxe_number),
                                               premium_number=int(
                                                   premium_number),
                                               suite_number=int(suite_number))
        hotel_booking_instance.save()

        recent_destination = hotel_booking_instance.hotel.location
        recent_destination_id = hotel_booking_instance.hotel.location.id
        print(recent_destination_id)
        recent_date = hotel_check_out
        print(recent_date)

        flight_possible_id = Flight.objects.filter(source=recent_destination_id, date=recent_date).values_list('id', flat=True)
        flight_possible_id_list = random.sample(list(flight_possible_id), min(len(flight_possible_id), 3))
        flight_possible = Flight.objects.filter(id__in=flight_possible_id_list)

        summary_data = {'recent_date': recent_date, 'recent_destination': recent_destination, 'flight_possible': flight_possible, 'number_of_rooms': number_of_rooms, 'hotel': hotel_instance, 'hotel_check_in': hotel_check_in_formatted, 'hotel_check_out': hotel_check_out_formatted,
                        'days': days.days, 'price_per_night': price_per_night, 'total_price': total_price}
        return render(request, "hotel_final_summary.html", summary_data)
