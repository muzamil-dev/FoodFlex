import mongoengine as me

class Item(me.Document):
    title = me.StringField(required=True)
    safe = me.BooleanField(required=True)
