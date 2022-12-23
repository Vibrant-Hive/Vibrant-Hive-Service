from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

# app_name = 'polls'
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

from django.urls import path

from . import views

app_name = 'mentors'
urlpatterns = [
    path('createAccount/', csrf_exempt(views.create_account), name='createAccount'),
]
