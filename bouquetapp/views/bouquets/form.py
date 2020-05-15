import sqlite3
from django.shortcuts import render
from bouquetapp.models import Bouquet
from ..connection import Connection

def bouquet_form(request):
    if request.method == 'GET':
        template = "bouquets/form.html"
        context = {}

        return render(request, template, context)