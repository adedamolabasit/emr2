from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from app import views
urlpatterns = [
    path('api/',views.apioverview,name='apiviewpoint'),
    path('api/emr-list/',views.emr_list,name='emr-list'),
    path('api/emr-detail/<int:pk>',views.emr_detail,name='emr-detail'),
    path('api/emr-update/<int:pk>',views.emr_update,name='emr-update'),
    path('api/emr-create/',views.emr_create,name='emr-create'),
    path('api/emr-delete/<int:pk>/',views.emr_delete,name='emr-delete'),
 
]