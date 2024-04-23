from django.db import models
from main.models import User

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title.lower()}"
    
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(blank=True, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class TableReservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveIntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    take_away = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, through='CartItem')
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"{self.quantity} x {self.item.name}"
    
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order {self.order.id}"
    
class KitchenOrder(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    ready = models.BooleanField(default=False)

    def __str__(self):
        return f"Kitchen Order for Order {self.order.id}"
    
class Testimonial(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.author