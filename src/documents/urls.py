from django.urls import path
from documents import views

urlpatterns = [
    path('quotes/', views.QuoteListView.as_view(), name='quote_list'),
    path('quote/pdf/<int:pk>/', views.QuotePDFView.as_view(), name='quote_pdf'),
]
