from django.urls import path
from . import views

urlpatterns = [
    path('', views.GeneralView.as_view(), name='all'),
    path('verbose', views.GeneralView.as_view(), name='verbose'),
    path('new', views.new_entry, name='new'),
    path('details/<int:pk>', views.DetailView.as_view(), name='app-detail'),
    path('details/<int:pk>/submit', views.update, name='app-post-detail'),
]
