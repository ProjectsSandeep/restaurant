from rest_framework import serializers
from .models import TableReservation, MenuItem

class TableReservationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=20)
    date = serializers.DateField()
    time = serializers.TimeField()
    people = serializers.IntegerField()
    message = serializers.CharField(max_length=1000)
    
    class Meta:
        model = TableReservation
        fields = ['name', 'email', 'phone', 'date', 'time', 'people','message']
        
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        return TableReservation.objects.create(**validated_data)
    
class OrderSerializer(serializers.Serializer):
    items = serializers.ListField(child=serializers.IntegerField())
    
    def validate(self, attrs):
        for item in self.items:
            if not MenuItem.objects.filter(id=item).exists():
                raise serializers.ValidationError(f"Menu item with id {item} does not exist")
        return attrs
    
    def create(self, validated_data):
        return super().create(validated_data)