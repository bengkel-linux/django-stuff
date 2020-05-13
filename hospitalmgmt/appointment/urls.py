from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:pk>', views.index, name='app-detail'), #TODO: replace the vies.index to the appropriate
]
