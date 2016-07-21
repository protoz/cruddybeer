import datetime
from flask import url_for
from cruddybeer import db

class Beer(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    description = db.StringField(verbose_name="Beer", required=True)
    name = db.StringField(verbose_name="Name", max_length=255, required=True)

#Check if the brewery currently exists, if it does not, add brewery
class Brewery(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    name = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    description = db.StringField(required=True)
    beers = db.ListField(db.EmbeddedDocumentField('Beer'))

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.name

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }

#Check if the brewery currently exists, if it does, remove brewery
def brewery_remove():
    return "Remove Brewery"

#Check if beer exists in selected brewery, if it does, remove it
def beer_remove():
    return "Remove Beer"