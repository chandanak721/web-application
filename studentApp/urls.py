from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.get_all_students, name='get_all_students'),
    path('students/create/', views.register_user, name='register_user'),
    path('students/<int:pk>/', views.get_student_by_id, name='get_student_by_id'),
    path('students/<int:pk>/update/', views.update_student, name='update_student'),
    path('students/<int:pk>/delete/', views.delete_student, name='delete_student'),
  
]


