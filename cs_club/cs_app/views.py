from django.shortcuts import render
from django.views import generic
from .models import *

class HomeView (generic.ListView):
    model=display
    template_name ="display_base_home.html"


class membermembersDetailView (generic.DetailView):
    model=member
    template_name ="member_list_members.html"


class membermembersListView (generic.ListView):
    model=member
    template_name ="member_base_members.html"


class projectprojectsDetailView (generic.DetailView):
    model=project
    template_name ="project_list_projects.html"


class projectprojectsListView (generic.ListView):
    model=project
    template_name ="project_base_projects.html"


class triptripsListView (generic.ListView):
    model=trip
    template_name ="trip_base_trips.html"


class displayaboutListView (generic.ListView):
    model=display
    template_name ="display_base_about.html"


class triptripsDetailView (generic.DetailView):
    model=trip
    template_name ="trip_list_trips.html"


