class triptripsListView (generic.ListView):
    model=trip
    template_name ="trip_base_trips.html"


class triptripsDetailView (generic.DetailView):
    model=trip
    template_name ="trip_list_trips.html"


