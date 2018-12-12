from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from cruddybeer.models import Beer, Brewery
from cruddybeer import app

breweries = Blueprint("breweries", __name__, template_folder="templates")


class ListView(MethodView):
    def __init__(self):
        pass

    def get(self):
        all_breweries = Brewery.objects.all()
        return render_template("list.html", breweries=all_breweries)


class DetailView(MethodView):
    def __init__(self):
        pass

    def get(self, slug):
        brewery = Brewery.objects.get_or_404(slug=slug)
        return render_template("detail.html", brewery=brewery)


# Register the urls
breweries.add_url_rule("/", view_func=ListView.as_view("list"))
breweries.add_url_rule("/<slug>/", view_func=DetailView.as_view("detail"))
