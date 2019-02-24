from flask import Blueprint, render_template
from flask.views import MethodView
from cruddybeer.models import Brewery

breweries = Blueprint("breweries", __name__, template_folder="templates")


@breweries.route('/')
def index():
    return render_template("index.html", methods=['GET'])


class ListBreweriesView(MethodView):
    def __init__(self):
        pass

    @staticmethod
    @breweries.route('/breweries', methods=['GET'])
    def get_brewery_list():
        all_breweries = Brewery.objects.all()
        return render_template("list.html", breweries=all_breweries)


class DetailBreweriesView(MethodView):
    def __init__(self):
        pass

    @staticmethod
    def get_brewery_detail(slug):
        brewery = Brewery.objects.get_or_404(slug=slug)
        return render_template("detail.html", brewery=brewery)


# Register the urls
breweries.add_url_rule("/", view_func=ListBreweriesView.as_view("list"))
breweries.add_url_rule("/<slug>/", view_func=DetailBreweriesView.as_view("detail"))
