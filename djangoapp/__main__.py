import django
import os
from djangoapp.models import Item
from djangoapp.models import Event
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoProduct.settings'
django.setup()


item1 = Item.objects.create()
item2 = Item.objects.create()
event1 = Event.objects.create(date='10-10-2020 19:00:00')
event2 = Event.objects.create(date='07-25-2018')
