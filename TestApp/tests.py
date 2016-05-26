import os,sys
import django

sys.path.append(".")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TestApp.settings")
django.setup()

from TestApp.models import *
#e=employee.objects.create(name="Mohamed",address="Cairo",age=31)
#e=employee()
#e.name="Ahmed2"
#e.address="Giza"
#e.age=29
#e.save()

e=employee.objects.get(id=5)
e.name="Hany"
e.save("Majed")