from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from cruddybeer.models import Beer, Brewery

breweries = Blueprint("breweries", __name__, template_folder="templates")


class ListBreweriesView(MethodView):
    def __init__(self):
        pass

    def get_brewery_list(self):
        all_breweries = Brewery.objects.all()
        return render_template("list.html", breweries=all_breweries)


class DetailBreweriesView(MethodView):
    def __init__(self):
        pass

    def get_brewery_detail(self, slug):
        brewery = Brewery.objects.get_or_404(slug=slug)
        return render_template("detail.html", brewery=brewery)


# Register the urls
breweries.add_url_rule("/", view_func=ListBreweriesView.as_view("list"))
breweries.add_url_rule("/<slug>/", view_func=DetailBreweriesView.as_view("detail"))
