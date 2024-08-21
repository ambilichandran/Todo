from django.db import models
class Todo(models.Model):
    items=models.CharField(max_length=50,blank=None)

    def __str__(self):
        return self.items