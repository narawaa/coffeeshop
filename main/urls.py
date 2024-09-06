from django.urls import path
from main.views import frontpage

app_name = 'main'

urlpatterns = [
    path('', frontpage, name='frontpage'),
]