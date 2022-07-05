from typing import Counter
from django.shortcuts import render, redirect
from .models import inventory_list
from datetime import datetime, timedelta
from django.db.models import Count
import pandas as pd
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    entries = inventory_list.objects.all()
    price = inventory_list.objects.filter(price__gt=10000)
    date = inventory_list.objects.filter(date_purchase__lt=datetime.now()-timedelta(days=5*365))
    ownerTotal = inventory_list.objects.values('user').annotate(total=Count('user')).order_by('-user')
    locTotal = inventory_list.objects.values('loc').annotate(total=Count('loc')).order_by('loc')
    context = {'entries' : entries , 'price':price, 'date':date, 'ownerTotal':ownerTotal,'locTotal':locTotal} # Store the data in "context" dictionaries
    return render(request,'inventory/index.html',context)

