from django.db import models
from task_manager.user.models import User

# Create your models here.
class Statuses(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
    )
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name
