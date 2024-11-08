from rest_framework import viewsets
from .models import Access, Users
from .serializers import AccessSerializer, UsersSerializer

class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
