from django.db import models
from models import *
from django.utils import timezone
class ModelTracker(models.Model):
    def __init__(self,*args,**kwargs):
        models.Model.__init__(self, *args, **kwargs)
        self.old_state = self.__dict__.copy()

    def save(self, username, force_insert=False, force_update=False, using=None, update_fields=None):
        history = History()
        history.table = self._meta.db_table
        history.done_on = timezone.now()
        history.done_by = username

        history.new_state = self.__dict__.copy()
        history.new_state.pop("old_state")

        if self.pk == None:
            history.old_state = {}
        else:
            history.old_state=self.old_state

        models.Model.save(self,force_insert=force_insert,force_update=force_update,using=using,update_fields=update_fields)
        history.primary_key=self.pk
        history.new_state.pop("_state","")
        history.old_state.pop("_state","")
        history.save()
