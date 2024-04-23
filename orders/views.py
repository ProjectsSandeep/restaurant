from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Menu, MenuItem, Order, OrderItem, Testimonial
from .serializers import TableReservationSerializer, OrderSerializer

# Create your views here.
def index(request):
    testimonials = Testimonial.objects.all()[:10]
    return render(request, "index.html", { 'testimonials': testimonials})

def menu(request):
    menus = Menu.objects.all()
    return render(request, "menu.html", {'menus': menus})

def events(request):
    return render(request, "events.html")

def cart(request):
    return render(request, "cart.html")

def reserve_table(request):
    if request.method == "POST":
        serializer = TableReservationSerializer(request)
    return render(request, "reserve_table.html")

def place_order(request, order_id):
    if request.method == "POST":
        order = Order.objects.get(id=order_id)
        serializer = OrderSerializer(data=request.POST)
        if serializer.is_valid():
            order_item = OrderItem(
                order=order,
                menu_item=serializer.validated_data['menu_item'],
                quantity=serializer.validated_data['quantity']
            )
            order_item.save()
            return HttpResponseRedirect(reverse('place_order.html'))
        else:
            errors = serializer.errors
            return render(request, 'place_order.html', {'errors': errors, 'form_data': serializer.data })
    return HttpResponseRedirect(reverse('place_order.html'))