import mongoengine as me

class Recipe(me.Document):
    name = me.StringField(required=True)
    ingredients = me.ListField(me.StringField(), required=True)
    description = me.StringField()
