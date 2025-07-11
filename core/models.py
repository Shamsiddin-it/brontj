from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='subcategories')
    icon = models.ImageField(upload_to="categories/", blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        full_name = self.name
        if self.parent:
            full_name = f"{self.parent.name} > {self.name}"
        return full_name
