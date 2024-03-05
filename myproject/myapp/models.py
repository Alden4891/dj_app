from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    item = models.CharField(max_length=100)
    code = models.CharField(max_length=100, default='default_value')
    qnt = models.IntegerField(null=True)
    description = models.TextField()

    def __str__(self):
        return self.item