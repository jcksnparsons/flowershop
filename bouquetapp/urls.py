from django.urls import path
from .views import *

app_name = "bouquetapp"

urlpatterns = [
    path('', bouquet_list, name="home"),
    path('bouquet/form', bouquet_form, name="bouquet_form")
]
