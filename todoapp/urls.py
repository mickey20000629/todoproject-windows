from . import views
from .views import TaskList, TaskDetail
from django.urls import path

urlpatterns = [
    path("", TaskList.as_view()),
    path("task/<int:pk>/", TaskDetail.as_view(), name='task')
]