from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    user_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    PENDING = 'Pending'
    DONE = 'Done'
    TASK_TYPE_CHOICES = [
        (PENDING, 'Pending'),
        (DONE, 'Done'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_detail = models.TextField()
    task_type = models.CharField(max_length=10, choices=TASK_TYPE_CHOICES)

    def __str__(self):
        return self.task_detail
