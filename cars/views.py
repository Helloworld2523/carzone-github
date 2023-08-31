from django.shortcuts import render

from cars.models import Car

# Create your views here.
def cars(request):
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    data = {
        'featured_cars':featured_cars
    }
    return render(request, 'cars/cars.html',data)