from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Access, Users, Record
from .serializers import AccessSerializer, UsersSerializer, RecordSerializer

class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer

    # Override retrieve method for custom GET by ID
    def retrieve(self, request, pk=None):
        try:
            access = Access.objects.get(pk=pk)
            serializer = AccessSerializer(access)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Access.DoesNotExist:
            return Response({"message": "Access record not found"}, status=status.HTTP_404_NOT_FOUND)

    # Override destroy method for custom DELETE by ID
    def destroy(self, request, pk=None):
        try:
            access = Access.objects.get(pk=pk)
            access.delete()
            return Response({"message": "Access record deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Access.DoesNotExist:
            return Response({"message": "Access record not found"}, status=status.HTTP_404_NOT_FOUND)

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

# Custom login view
@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    # Simple email and password check
    try:
        user = Access.objects.get(email=email, password=password)
        return Response({'message': 'Login successful', 'status': 'ok'}, status=status.HTTP_200_OK)
    except Access.DoesNotExist:
        return Response({'message': 'Invalid credentials', 'status': 'error'}, status=status.HTTP_401_UNAUTHORIZED)
