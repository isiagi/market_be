from django.db import models

# Create your models here.
class Category(models.Model):
    """Hierarchical category system"""
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, 
                             on_delete=models.CASCADE, 
                             related_name='subcategories')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} > {self.name}"
        return self.name
