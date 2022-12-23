from django.views.decorators.csrf import csrf_exempt
from django.urls import path

from . import views

app_name = 'mentors'
urlpatterns = [
    path('createAccount/', csrf_exempt(views.create_account), name='createAccount'),
]
