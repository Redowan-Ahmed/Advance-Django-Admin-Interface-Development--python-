from django.db import models
from ckeditor.fields import RichTextField
from status.models import Status
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    descripstion = RichTextField()
    image = models.ImageField(upload_to="media/todoimages")
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    schedule = models.DateTimeField(null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title
