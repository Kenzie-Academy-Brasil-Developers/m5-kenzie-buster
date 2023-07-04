from django.db import models


class SizeRating(models.TextChoices):
    size_g = "G"
    size_pg = "PG"
    size_13 = "PG-13"
    size_r = "R"
    size_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, default=None, null=True)
    rating = models.CharField(
        max_length=20, choices=SizeRating.choices, default=SizeRating.size_g, null=True
    )
    synopsis = models.TextField(null=True, default=None)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )

    buyers = models.ManyToManyField(
        "users.User", through="movies.MovieOrder", related_name="user_Movie"
    )


class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)

    price = models.DecimalField(max_digits=8, decimal_places=2)

    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="movie_order"
    )

    buyer = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_order"
    )
