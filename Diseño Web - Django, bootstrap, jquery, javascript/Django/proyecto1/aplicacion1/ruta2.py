from django.conf.urls import url
from aplicacion1 import views

urlpatterns = [
    url('home/',views.vista2,name='vista2'),
]