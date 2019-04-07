from django.db import models

# Create your models here.


class DataModel(models.Model):
    class Meta:
        app_label = 'game'
    ip = models.CharField(max_length=20)
    code_id = models.IntegerField(null=True)
    type = models.IntegerField()
    ans = models.CharField(max_length=200, null=True)
    flag = models.BooleanField()
    input = models.CharField(max_length=200, null=True)
    marks = models.CharField(max_length=200, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)