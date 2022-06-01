from uuid import uuid4
from account.models import User
from django.db import models
from django.urls import reverse
# Create your models here.

class UUIDModel(models.Model):
    uuid = models.UUIDField(
        default=uuid4, unique=True, editable=False, verbose_name="UUID"
    )

class Item(UUIDModel):
    COMPLETED = 'completed'
    PENDING = 'pending'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed')
    )
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Task Name")
    scheduled_at = models.DateTimeField()
    status = models.CharField(
        max_length=50,
        default=PENDING,
        choices=STATUS_CHOICES,
        verbose_name='Task Status'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("items")
    