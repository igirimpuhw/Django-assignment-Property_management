from django.db import models

Property_type=(
    ('Apartment', 'Apartment'),
    ('Commercial', 'Commercial'),
    ('House', 'House'),
)
#models for property
class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    property_type = models.CharField(max_length=100, choices=Property_type)
    Number_unit = models.IntegerField()
    description = models.TextField()
    class meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.name

#models of Units
class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    Unit_number = models.IntegerField()
    bedrooms= models.IntegerField()
    bathrooms= models.IntegerField()
    rent = models.IntegerField()
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.property.name

#models of tenant

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    Phone_number = models.CharField(max_length=100)
    def __str__(self):
        return self.name

#models of Lease
class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.IntegerField()
    def __str__(self):
        return self.tenant.name



#property_management

