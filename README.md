# Cruddy Beer is a CRUD exercise using Flask.

From this, a user will be able to do the following:

- add/remove a brewery
- add/remove a beer to a chosen brewery

## Requirements
pip install flask
pip install mongoengine


## What you can currently do:

### Add a Brewery and associate a beer using the manage.py
*
python manage.py shell

from cruddybeer.models import Beer, Brewery
brewery = Brewery(
name = "Brewery Name",
slug = "brewery-name",
description = "Brewery Description"
)
brewery.save()

beer = Beer(
name="Beer Name",
description="Beer Description"
)
brewery.beers.append(beer)
brewery.save()
*

You will now have a collection in the test database of MongoDB called brewery.


## Starting Cruddybeer
Start the flask application with python run.py

## Future To-Do
- Add proper testing
- Add a UI to add breweries and beer
- Add the ability to manage and remove items