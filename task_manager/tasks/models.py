from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.user.models import User
from task_manager.statuses.models import Statuses


# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="author",
        verbose_name=_("Author"),
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="executor",
        verbose_name=_("Executor"),
    )
    status = models.ForeignKey(Statuses, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
