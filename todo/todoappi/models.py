from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime


class Todo(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    status = models.BooleanField()
    created_at = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        title = self.title
        description = self.description
        status = self.status
        created_at = self.created_at

        return '{}{}{}{}'.format(self.title, self.description,self.status,self.created_at)
