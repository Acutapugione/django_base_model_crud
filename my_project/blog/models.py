from typing import Iterable
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=450)

    def __str__(self):
        return f"Post: {self.title} :=> {self.text}"
    
class PostSettings(models.Model):
    title_len = models.IntegerField()
    text_len = models.IntegerField()

    def save(self, *args, **kwargs) -> None:
        self.pk = 1
        # super(SingletonModel, self).save(*args, **kwargs)
        return super().save(*args, **kwargs)
    
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj