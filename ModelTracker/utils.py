from functools import lru_cache

from django.apps import apps


@lru_cache(50)
def get_model(table_name):
    return next((m for m in apps.get_models() if m._meta.db_table==table_name), None)

def get_fields(model):
    return [f.name for f in model._meta.get_fields()]