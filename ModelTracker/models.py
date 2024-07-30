import datetime
from functools import lru_cache

from django.db import models
from django.apps import apps

from ModelTracker.utils import get_fields,get_model


try:
    from django.db.models import JSONField
except ImportError:
    try:
        from jsonfield.fields import JSONField
    except ImportError:
        raise ImportError("Can't find a JSONField implementation, please install jsonfield if django < 4.0")


class History(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,default="")
    table=models.CharField(max_length=255)
    primary_key=models.CharField(max_length=255)
    # old_state=JSONField(default=dict)
    new_state=JSONField(default=dict)
    done_by=models.CharField(max_length=255)
    done_on=models.DateTimeField(auto_now_add=True)

    def get_object(self):
        model = get_model(self.table)
        fields = get_fields(model)
        keys2del = []
        state = self.new_state
        for key in state:
            if (key.startswith("_") and "_cache" in key) or (key not in fields and not ("_id" in key and key[:-3] in fields)):
                keys2del.append(key)
            if type(state[key])==type({}):
                if state[key].get("_type",None) == "datetime":
                    state[key]=datetime.datetime.strptime(state[key]["value"],"%Y-%m-%d %H:%M:%S")
                elif state[key].get("_type",None) == "date":
                    state[key]=datetime.datetime.strptime(state[key]["value"],"%Y-%m-%d")
        for key in keys2del:
            del state[key]
        return model(**state)

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        if self.name:
            return "%s for %s in %s"%(self.name, self.primary_key, self.table)
        return "%s in %s"%(self.primary_key, self.table)

    def __unicode__(self):
        return self.__str__()

