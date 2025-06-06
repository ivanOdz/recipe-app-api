"""
Views for the user API
"""


from rest_framework import generics

from user.serializers import UserSerializer

# CreateAPIView handles POST requests
class CreateUserAPIView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer
