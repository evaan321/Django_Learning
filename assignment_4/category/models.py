from django.db import models


# Create your models here.
class TaskCategory(models.Model):
    
    categoryName = models.CharField(max_length=20, default = "Specially" )

    def __str__(self) -> str:
        return f'{self.categoryName}'