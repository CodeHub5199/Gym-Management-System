from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('registration', views.registration, name='registration'),
    path('manage_members', views.manage_members, name='manage_members'),
    path('update_members/<int:member_id>/', views.update_member, name='update_member'),
    path('show_member/<int:member_id>/', views.show_member, name='show_member'),
    path('update_fees', views.update_fees, name='update_fees'),
    path('manage_trainer', views.manage_trainer, name='manage_trainer'),
    path('delete_member/<int:member_id>/', views.delete_member, name='delete_member'),
    path('delete_trainer/<int:trainer_id>/', views.delete_trainer, name='delete_trainer'),
]