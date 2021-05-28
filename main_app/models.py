from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.


class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Craft(models.Model):
    # from API
    cargo_capacity = models.BigIntegerField()
    consumables = models.CharField(max_length=100)
    cost_in_credits = models.BigIntegerField()
    crew = models.IntegerField()
    length = models.DecimalField(decimal_places=10, max_digits=20)
    manufacturer = models.CharField(max_length=500)
    max_atmosphering_speed = models.IntegerField()
    model = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    passengers = models.IntegerField()
    hyperdrive_rating = models.FloatField()
    # may or may not exist
    starship_class = models.CharField(max_length=100)
    MGLT = models.CharField(max_length=100)
    # own stuff
    sell_price = models.IntegerField()
    BUCKET = 'Bucket'
    FAIR = 'Fair'
    GOOD = 'Good'
    EXCELLENT = 'Excellent'
    LIKE_NEW = 'Like New'
    CONDITION = (
        (BUCKET, 'Bucket'),
        (FAIR, 'Fair'),
        (GOOD, 'Good'),
        (EXCELLENT, 'Excellent'),
        (LIKE_NEW, 'Like New'),
    )
    condition = models.CharField(max_length=100, choices = CONDITION, default = GOOD)
    description = models.TextField(max_length=1000)
    mileage = models.IntegerField()
    date_created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badges = models.ManyToManyField(Badge)
    color = models.CharField(max_length=100, blank=True)
    black = models.CharField(max_length=100, blank=True)

    def __str__(self): 
        return self.name

    def get_absolute_url(self):
        return reverse('crafts')

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    craft = models.ForeignKey(Craft, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return f"{self.craft_id}"

class Photo(models.Model):
    url = models.CharField(max_length=200)
    craft = models.ForeignKey(Craft, on_delete=models.CASCADE)


    def __str__(self):
        return f"Photo for craft_id: {self.craft_id} @{self.url}"

class Spacecraft(models.Model):
    cargo_capacity = models.BigIntegerField()
    consumables = models.CharField(max_length=100)
    cost_in_credits = models.BigIntegerField()
    crew = models.IntegerField()
    length = models.DecimalField(decimal_places=10, max_digits=20)
    manufacturer = models.CharField(max_length=500)
    max_atmosphering_speed = models.IntegerField()
    model = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    passengers = models.IntegerField()
    hyperdrive_rating = models.FloatField()
    MGLT = models.IntegerField()
    starship_class = models.CharField(max_length=100)
    color = models.CharField(max_length=200)
    black = models.CharField(max_length=200)
