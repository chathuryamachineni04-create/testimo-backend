from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import User
from .models import Testimonial
from .serializers import TestimonialSerializer


class TestimonialViewSet(viewsets.ModelViewSet):
    serializer_class = TestimonialSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Testimonial.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PublicTestimonialView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, username):
        try:
            owner = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {"error": "Owner not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = TestimonialSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(
                owner=owner,
                status="Pending",
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)