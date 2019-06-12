from django.db import models

# Create your models here.

class Detail(models.Model):
    """
    Define database schema
    """
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name