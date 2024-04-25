from django.db import models

# Create your models here.
class Movie(models.Model): 
 rating_choices = (
  ('G', 'General audiences'),
  ('PG', 'Parental guidance suggested'),
  ('PG-13', 'Parents strongly cautioned'),
  ('R', 'Restricted'),
  ('NC-17', 'Adults Only')
    )

 title = models.CharField(max_length=127)
 duration = models.CharField(max_length=10, blank=True, default='', null=True)
 rating = models.CharField(max_length=20, choices=rating_choices, default='G')
 synopsis = models.TextField(blank=True, default='') 

 user = models.ForeignKey(
   "users.User", on_delete=models.CASCADE, related_name="owner", null=True
   )
 
 order = models.ManyToManyField(
  "users.User", through="movies_orders.MovieOrder"
 )
 

