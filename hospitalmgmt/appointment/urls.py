from django.urls import path
from . import views

urlpatterns = [
    path('', views.GeneralView.as_view(), name='all'),
    path('new', views.new_entry, name='new'),
    path('details/<int:pk>', views.DetailView.as_view(), name='app-detail'),
]
