from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=100)
    code = models.CharField(max_length=100, default='0')
    key1 = models.IntegerField(null=True, default=0)
    key2 = models.IntegerField(null=True, default=0)
    key3 = models.IntegerField(null=True, default=0)
    description = models.TextField()

    def __str__(self):
        return self.item

class Item_details(models.Model):
    detail_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE,null=True)  # this will create item_id
    code = models.CharField(max_length=100, default='0')
    date_time = models.DateTimeField()
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return self.item

        