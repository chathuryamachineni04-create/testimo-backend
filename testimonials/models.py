from django.db import models
from django.conf import settings


class Testimonial(models.Model):

    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Published", "Published"),
    )

    customer = models.CharField(max_length=100)

    company = models.CharField(
        max_length=100,
        blank=True,
    )

    message = models.TextField()

    rating = models.IntegerField(default=5)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="testimonials",
    )

    def __str__(self):
        return self.customer