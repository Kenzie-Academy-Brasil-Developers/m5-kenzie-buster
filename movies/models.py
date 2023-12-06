from django.db import models


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
    synopsis = models.CharField(
        max_length=999,
        blank=True,
        default="")
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies"
    )
