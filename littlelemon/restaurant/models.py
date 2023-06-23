from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.name


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.first_name


# Add code to create Menu model
class Menu(models.Model):
    name = models.CharField(max_length=200) 
    price = models.IntegerField(null=False) 
    menu_item_description = models.TextField(max_length=1000, default='')
    # New field for inventory
    inventory = models.PositiveIntegerField(default=100)
    
    def __str__(self):
      return f'{self.name} : {str(self.price)}'
