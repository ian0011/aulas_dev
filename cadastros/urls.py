from django.urls import path
from cadastros import views

app_name = 'cadastros'

urlpatterns = [
    path('', views.index, name='index' ),
]
