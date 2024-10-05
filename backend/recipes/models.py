from mongoengine import Document, StringField

class Recipe(Document):
    title = StringField(required=True, max_length=200)
    description = StringField()
    ingredients = StringField()  # Make ingredients a text field
    instructions = StringField()

    def __str__(self):
        return self.title
