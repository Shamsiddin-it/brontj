from django.urls import path
from .views import ServiceViewSet

service_list = ServiceViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

service_detail = ServiceViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
service_upload_image = ServiceViewSet.as_view({
    'post': 'upload_image',
})

urlpatterns = [
    path('', service_list, name='service-list'),
    path('<int:pk>/', service_detail, name='service-detail'),
    path('<int:pk>/upload-image/', service_upload_image, name='service-upload-image'),

]
