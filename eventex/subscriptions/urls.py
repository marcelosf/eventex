from django.urls import path
from eventex.subscriptions.views import subscribe
from eventex.subscriptions.views import detail

app_name = 'subscriptions'

urlpatterns = [
    path('inscricao/', subscribe, name='new'),
    path('inscricao/<int:pk>/', detail, name='detail'),
]