from rest_framework import permissions
from .models import Category, ToDo
from .serializers import ToDoSerializer, CategorySerializer
from .permissions import IsAuthorOrAdmin
from rest_framework.viewsets import ModelViewSet


class ToDoView(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def get_permissions(self):
        if self.action in ('destroy', 'update', 'partial_update'):
            return IsAuthorOrAdmin(),
        return permissions.IsAuthenticatedOrReadOnly(),

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = permissions.IsAdminUser,
