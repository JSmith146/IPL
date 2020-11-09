from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('', views.show_login),
    path('registration', views.show_registration),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    # path('all_projects', views.show_all),
    path('new_project', views.create_project),
    path('project/<int:id>', views.show_project),
    # path('test', views.test),
    #New 
    path('all_projects', views.show_all),
    path('flight/<str:flight_name>', views.show_flight),
    path('project/<int:id>/add_comment', views.add_comment),
    path('project/<int:id>/edit', views.edit_project)
]