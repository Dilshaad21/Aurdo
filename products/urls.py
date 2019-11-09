from django.urls import path
from .views import *

app_name = "products"

urlpatterns = [
    path('', index, name="index"),
    path('add_product/', add_product, name="add-product"),
    path('menu/', menu, name="menu"),
    path('purchase/', purchase, name="purchase"),
    path('your_bill/',yourbill,name="bill"),
    path('sendmail/',sendmail,name="sendmail"),
]
