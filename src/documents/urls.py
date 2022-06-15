from django.urls import path
from documents import views

urlpatterns = [
    #path('', views.quote_list, name='quote_list'),
    #path('quote/<int:pk>/', views.quote_detail, name='quote_detail'),
    path('quote/new/', views.quote_new, name='quote_new'),
]