from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    path('todos/', views.SnippetList.as_view()),
    path('todos/<int:pk>/', views.SnippetDetail.as_view()),
]

