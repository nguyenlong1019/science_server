from django.urls import path, include 
from core.views.index import *


urlpatterns = [
    path('', index_view, name='index'),
    path('topics/<slug:slug>', topic_detail_view, name='topic-detail'),
    path('documents/<slug:slug>', document_detail_view, name='document-detail'),
]
