from django.db import models


# from movies.models import Movie
# from users.models import User
#

class MovieOrder(models.Model):
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    purchased_at = models.DateTimeField(auto_now_add=True)
