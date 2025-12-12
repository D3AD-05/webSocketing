from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    # Page
    path('', views.index, name='index'),

    # HTMX Partials
    path('students/', views.student_list, name='list'),
    path('students/create/', views.student_create, name='create'),
    path('students/<int:pk>/edit/', views.student_edit, name='edit'),
    path('students/<int:pk>/delete/', views.student_delete, name='delete'),
    path('students/<int:pk>/', views.student_detail, name='detail'),
]
