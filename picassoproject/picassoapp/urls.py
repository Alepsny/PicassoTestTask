from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.FileList.as_view(), name='file-list'),
    path('upload/<int:pk>/', views.FileDetail.as_view(), name='file-detail'),
]