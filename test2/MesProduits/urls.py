from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('del_prod/<int:id>', views.del_prod, name='del_prod')
    ]