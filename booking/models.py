from django.db import models
from django.contrib.auth.models import User

# Movie model
class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    duration = models.IntegerField()  # Duration in minutes
    description = models.TextField()

    def __str__(self):
        return self.title

# Showtime model
class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    showtime_date = models.DateField()
    showtime_time = models.TimeField()
    available_seats = models.IntegerField()
    total_seats = models.IntegerField()

    def __str__(self):
        return f"{self.movie.title} - {self.showtime_time}"

# Booking model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seats_booked = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.showtime.movie.title} ({self.seats_booked} seats)"
