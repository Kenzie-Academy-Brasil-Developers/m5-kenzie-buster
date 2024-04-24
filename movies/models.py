from django.db import models

# Create your models here.
class Movie(models.Model):
 title = models.CharField(max_length=127)
 duration = models.CharField(max_length=10, null=True)
 rating = models.CharField(max_length=20, default='G')
 synopsis = models.TextField(null=True)

 user = models.ForeignKey(
   "users.User", on_delete=models.CASCADE, related_name="owner", null=True
   )
 
 order = models.ManyToManyField(
  "users.User", through="movies_orders.MovieOrder"
 )
 

