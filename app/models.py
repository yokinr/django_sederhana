from django.db import models
from django.urls import reverse
import uuid
from django_generic.ckeditor_config import *
from ckeditor.fields import RichTextField


class ModelName(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    field1 = models.CharField(max_length=100)
    field2 = models.TextField()
    field3 = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.field1
