import mongoengine as me
from recipes.models import Recipe
from mongoengine.fields import ListField

class User(me.Document):
    username = me.StringField(required=True, unique=True)
    email = me.EmailField(required=True, unique=True)
    password = me.StringField(required=True)
    favorite_recipes = me.ListField(me.ReferenceField('Recipe'))
    item_ids = ListField()

    RELIGIOUS_RESTRICTIONS_OPTIONS = [
        'None',
        'Halal',
        'Kosher',
        'Hindu Vegetarian',
    ]
    
    DIET_OPTIONS = [
        'None',
        'Vegetarian',
        'Vegan',
        'Paleo',
        'Keto',
        'Gluten-Free',
        'Pescatarian',
        'Lacto-Vegetarian',
        'Ovo-Vegetarian',
        'Lacto-Ovo-Vegetarian',
        'Whole30',
        'Low-Carb',
        'Mediterranean',
        'Diabetic-Friendly',
        'Low-FODMAP',
        'DASH',
        'Low-Sodium',
        'High-Protein',
    ]
    
    ALLERGY_OPTIONS = [
        'Peanuts',
        'Tree Nuts',
        'Milk',
        'Eggs',
        'Wheat',
        'Soy',
        'Fish',
        'Shellfish',
        'Gluten',
        'Sesame',
        'Mustard',
        'Corn',
        'Lupin',
        'Mollusks',
        'Sulphites',
        'Celery',
        'Fruits',
        'Legumes',
        'Meat',
        'Dairy',
        'Nightshades',
    ]

    RELIGIOUS_RESTRICTIONS_CHOICES = [(option, option) for option in RELIGIOUS_RESTRICTIONS_OPTIONS]
    DIET_CHOICES = [(option, option) for option in DIET_OPTIONS]
    ALLERGY_CHOICES = [(option, option) for option in ALLERGY_OPTIONS]

    religious_restrictions = me.StringField(
        choices=RELIGIOUS_RESTRICTIONS_CHOICES,
        default='None'
    )
    diet = me.StringField(
        choices=DIET_CHOICES,
        default='None'
    )
    allergies = me.ListField(
        me.StringField(choices=ALLERGY_OPTIONS),
        default=[]
    )


    def __str__(self):
        return self.username
