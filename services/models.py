from django.db import models
from accounts.models import User
from core.models import Category

def service_image_path(instance, filename):
    return f'services/{instance.provider.username}/{filename}'

class Service(models.Model):
    provider = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='services',
        limit_choices_to={'role': 'provider'}
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=service_image_path)

    def __str__(self):
        return f"Image for {self.service.title}"
