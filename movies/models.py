from django.db import models
from users.models import User


class RatingOptions(models.TextChoices):
    G = "G"
    PG = "PG"
    PG13 = "PG-13"
    R = "R"
    NC17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(
        max_length=10, blank=True, default=""
    )
    rating = models.CharField(
        max_length=20,
        choices=RatingOptions.choices,
        default=RatingOptions.G
    )
    synopsis = models.TextField(
        blank=True,
        default="")
    user = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        related_name="movies"
    )
    users = models.ManyToManyField(
        User, through="movies_orders.MovieOrder", related_name="movie_orders"
    )
