from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions

from .models import Employee
from .permissions import IsOwnerOrReadOnly
from .serializers import EmployeeSerializer, UserSerializer


class EmployeeList(generics.ListCreateAPIView):
    """Lists all employees or creates a new employee."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieves, updates, or deletes an employee instance."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class EmployeeListLevel(generics.ListAPIView):
    """Lists all employees of the same level."""
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        level = self.kwargs['level']
        return Employee.objects.filter(level=level)


class UserList(generics.ListAPIView):
    """Lists all users."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """Retrieves an employee instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
