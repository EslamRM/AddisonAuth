from django.urls import path
from .views import RequestTokenView

urlpatterns = [
    path('request-token/', RequestTokenView.as_view(), name='request-token'),
]
