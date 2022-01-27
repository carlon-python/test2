from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=173)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    description = models.CharField(max_length=174, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

def __str__(self):
    return f"{self.title}"