from django.urls import path
from . import views

urlpatterns = [
    path('add_user/', views.add_user, name='add_user'),
    path('add_task/', views.add_task, name='add_task'),
    path('user_list/', views.user_list, name='user_list'),
    path('task_list/', views.task_list, name='task_list'),
    path('export_to_excel/', views.export_to_excel, name='export_to_excel'),
]
