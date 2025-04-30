from django.db import models

class Host(models.Model):
    name = models.CharField(max_length=100)
    is_superhost = models.BooleanField(default=False)
    profile_url = models.URLField()

    def __str__(self):
        return self.name

class Listing(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    image_urls = models.JSONField()
    ratings = models.FloatField()
    description = models.TextField()
    number_of_reviews = models.IntegerField()
    amenities = models.JSONField()
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    property_type = models.CharField(max_length=100)

    def __str__(self):
        return self.title
