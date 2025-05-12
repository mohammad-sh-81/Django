from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('', views.all_todos),
    path('<int:event_id>', views.todo_detail_view),
]