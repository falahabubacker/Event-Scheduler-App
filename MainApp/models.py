from django.db import models
import arrow

class Amenity(models.Model):
    amenity = models.CharField(max_length=25)

    def __str__(self):
        return self.amenity

class Event(models.Model):
    
    TIME_CATEGORIES = [
        ("FULL", "Full Day"),
        ("FORE", "Half Day (Before Noon)"),
        ("AFTR", "Half Day (After Noon)")
    ]

    family_name = models.CharField(max_length=30)
    guardian_name = models.CharField(max_length=15)
    event_type = models.CharField(max_length=20)
    participants = models.PositiveIntegerField(blank=True)
    date = models.DateField()
    day = models.CharField(max_length=10, blank=True)
    month = models.CharField(max_length=10, blank=True)
    strt_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True)
    time_category = models.CharField(max_length=10, choices=TIME_CATEGORIES)
    location = models.CharField(max_length=100, blank=True)
    amenities = models.ManyToManyField(Amenity, blank=True, related_name="events")
    
    def __str__(self):
        return f"{self.guardian_name} {self.family_name} {str(self.date)}"
    
    def save(self, *args, **kwargs):
        date_obj = arrow.get(str(self.date), 'YYYY-MM-DD')
        self.day = date_obj.format('dddd')
        self.month = date_obj.format('MMMM')

        super().save(*args, **kwargs)