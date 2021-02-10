from django.urls import path
from . import views

urlpatterns = [
	path('', views.pred, name = 'prediction'),
]
