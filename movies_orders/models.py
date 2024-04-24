from django.db import models

# Create your models here.
class MovieOrder(models.Model):
 movie = models.ForeignKey(
  "movies.Movie", on_delete=models.CASCADE, related_name="movie_orders"
   )

 order = models.ForeignKey(
  "users.User", on_delete=models.CASCADE, related_name="user_movie_orders"
   )
 
 purchased_at = models.DateTimeField(auto_now_add=True)
 price = models.DecimalField(max_digits=8, decimal_places=2)


