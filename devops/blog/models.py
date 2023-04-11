from django.db import models
from devops.common.models import BaseModel


class Product(BaseModel):
    name=models.TextField(max_length=255)
# Create your models here.
