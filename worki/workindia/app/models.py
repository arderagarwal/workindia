from django.db import models

# Create your models here.
class Snippet(models.Model):
    due_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description= models.CharField(max_length=100, blank=True, default='')
    category = models.CharField(max_length=100, blank=True, default='')
    class Meta:
        ordering = ['due_date']
