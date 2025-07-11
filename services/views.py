from rest_framework import viewsets, permissions
from .models import Service
from .serializers import ServiceSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import ServiceImage
from .serializers import ServiceImageUploadSerializer
from django_filters.rest_framework import DjangoFilterBackend

class IsProviderOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.provider == request.user


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().select_related('provider', 'category').prefetch_related('images')
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsProviderOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(provider=self.request.user)
    
    @action(detail=True, methods=['post'], url_path='upload-image', permission_classes=[permissions.IsAuthenticated])
    def upload_image(self, request, pk=None):
        service = self.get_object()
        if service.provider != request.user:
            return Response({"detail": "Not allowed."}, status=status.HTTP_403_FORBIDDEN)

        serializer = ServiceImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(service=service)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'is_active', 'price']