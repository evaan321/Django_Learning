from django.db import models

from  category.models import TaskCategory
# Create your models here.

class TaskModel(models.Model):

    catName = models.ForeignKey(TaskCategory, on_delete=models.CASCADE, related_name='catName_tasks',default = 1)
    taskTitle = models.CharField(max_length=20)

    taskDetail = models.TextField()

    is_completed = models.BooleanField(default=False)

    assign = models.DateTimeField()

    category = models.ManyToManyField(TaskCategory)

    

    def __str__(self) -> str:
        return self.taskTitle