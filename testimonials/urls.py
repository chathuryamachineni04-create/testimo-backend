from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TestimonialViewSet, PublicTestimonialView

router = DefaultRouter()
router.register("testimonials", TestimonialViewSet, basename="testimonials")

urlpatterns = router.urls + [
    path(
        "public/testimonials/<str:username>/",
        PublicTestimonialView.as_view(),
        name="public-testimonial",
    ),
]