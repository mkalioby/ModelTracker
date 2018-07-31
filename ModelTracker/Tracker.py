from django.db import models
import sys
from .models import *
import copy
from django.utils import timezone
from django.contrib.admin.utils import NestedObjects
import threading

class ModelTracker(models.Model):
    thread = threading.local()
    def __init__(self,*args,**kwargs):
        models.Model.__init__(self, *args, **kwargs)
        self.old_state = copy.deepcopy(self.__dict__)



    def save(self, username='', event_name="",force_insert=False, force_update=False, using=None, update_fields=None):
        types=[]
        if username==None:
            models.Model.save(self,force_insert=force_insert,force_update=force_update,using=using,update_fields=update_fields)
            return
        if username=='':  username= self.thread.request.user.username
        if sys.version_info > (3,):
            lng=int
        else:
            lng=long
        types=[type("a"),type(1),type({}),type([]),type(("1",2)),type(True),type(lng(1)),type(u"a"),type(1.1),type(None)]
        history = History()
        history.table = self._meta.db_table
        history.done_on = timezone.now()
        history.done_by = username
        history.name=event_name
        x=self.__dict__.copy()
        history.new_state = copy.deepcopy(x)
        history.new_state.pop("old_state")

        if self.pk == None:
            history.old_state = {}
        else:
            history.old_state=self.old_state
        keys2del=[]
        for key in history.old_state:
            if type(history.old_state[key]) not in types:
                if hasattr(history.old_state[key],"toJSON"):
                    history.old_state[key]=history.old_state[key].toJSON()
                elif hasattr(history.old_state[key],"pk"):
                    history.old_state[key]= history.old_state[key].pk
                else:
                    keys2del.append(key)
        for key in keys2del:
            del history.old_state[key]
        keys2del=[]
        for key in history.new_state:
            if type(history.new_state[key]) not in types:
                if hasattr(history.new_state[key], "toJSON"):
                    history.new_state[key] = history.new_state[key].toJSON()
                elif hasattr(history.new_state[key], "pk"):
                    history.new_state[key] = history.new_state[key].pk
                else:
                    keys2del.append(key)
        for key in keys2del:
            del history.new_state[key]
        models.Model.save(self,force_insert=force_insert,force_update=force_update,using=using,update_fields=update_fields)
        history.primary_key=self.pk
        history.new_state.pop("_state","")
        history.old_state.pop("_state","")
        history.save()


    def delete(self, username='', event_name="", using=None, ):
        def format(obj):
            return "%s:%s" % (obj._meta.db_table, obj.pk)

        types = []
        if username == None:
            models.Model.delete(self, using=using)
            return
        if username == '':  username = self.thread.request.user.username
        if sys.version_info > (3,):
            lng = int
        else:
            lng = long
        types = [type("a"), type(1), type({}), type([]), type(("1", 2)), type(True), type(lng(1)), type(u"a"),
                 type(1.1), type(None)]
        history = History()
        history.table = self._meta.db_table
        history.done_on = timezone.now()
        history.done_by = username
        if event_name == '': event_name = "Delete"
        history.name = event_name

        history.old_state = self.old_state
        history.primary_key = self.pk
        history.new_state.pop("_state", "")
        history.old_state.pop("_state", "")
        history.new_state={"related_records":[]}

        collector = NestedObjects('default')
        collector.collect([self])
        x = collector.nested(format)
        if len(x) > 1:
            history.new_state["related_records"]=x[1]
        history.save()
        history.new_state.pop("_state", "")
        history.old_state.pop("_state", "")
        models.Model.delete(self, using=using)

    class Meta:
        abstract =True
