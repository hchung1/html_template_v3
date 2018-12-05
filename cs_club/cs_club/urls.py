from django.contrib import admin
from django.urls import path
from cs_app.views import *

urlpatterns=[
path('admin/', admin.site.urls),
path('',HomeView.as_view(),name="home"),
path('members/<int:pk>/',membermembersDetailView.as_view(),name="members"),
path('members/',membermembersListView.as_view(),name="members"),
path('projects/<int:pk>/',projectprojectsDetailView.as_view(),name="projects"),
path('projects/',projectprojectsListView.as_view(),name="projects"),
path('trips/',triptripsListView.as_view(),name="trips"),
path('about/',displayaboutListView.as_view(),name="about"),
path('trips/<int:pk>/',triptripsDetailView.as_view(),name="trips"),
]