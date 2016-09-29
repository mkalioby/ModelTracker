from django.db import models
from jsonfield import JSONField
class History(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,default="")
    table=models.CharField(max_length=255)
    primary_key=models.CharField(max_length=255)
    old_state=JSONField(default={})
    new_state=JSONField(default={})
    done_by=models.CharField(max_length=255)
    done_on=models.DateTimeField(auto_now_add=True)

