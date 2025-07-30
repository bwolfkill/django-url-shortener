from django.db import models

# Create your models here.
class URL(models.Model):
    hash = models.CharField(max_length=10, unique=True)
    url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    visits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.url
