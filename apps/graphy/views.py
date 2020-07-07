from django.shortcuts import render
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

import random

# Create your views here.
def homepage(request):

    # x = [ 1, 2, 3, 4, 5 ]
    # y = [ 1, 2, 3, 4, 5 ]

    # plot = figure(title = "Line Graph", x_axis_label="X-Axis", y_axis_label="Y-Axis", plot_width=400, plot_height=400)

    # plot.line(x, y, line_width=2)

    # script, div = components(plot)

    # return render(request, "graphy/index.html", {'script': script, 'div': div} )
    return render(request, "homepage.html", {})

def dashboard(request):

    name = random.randint(0, 100)
    print(name)

    return render(request, "dashboard.html", { 'name': name })