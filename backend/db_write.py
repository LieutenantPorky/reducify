from peewee import *
from playhouse.sqlite_ext import *

ingredientsDb = SqliteDatabase('ingredients.db')

db = SqliteDatabase('data.db')

class Ingredient(Model):
    name = CharField(unique=True)
    lifetime = IntegerField()

    class Meta:
        database = ingredientsDb


class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name = CharField(unique=True)
    password = CharField()
    id = AutoField()
    fridge = JSONField()












if __name__ == "__main__":
    ingredientsDb.create_tables([Ingredient])

    ingredients = [["name", 30],["Avocado", 5],["Bacon", 14],["Bananas", 7],["Bread", 7],["Butter", 270],["Cauliflower", 14],["Raw Chicken", 2],["Cucumber", 7],["Eggs", 35],["Feta cheese", 5],["Frozen Peas", 365],["Garlic", 150],["Kale", 7],["Milk", 7],["Onions", 60],["Pomegranate", 60],["Potatoes", 35],["Red onions", 60],["Salad", 5]]

    for i in ingredients:
        Ingredient(name=i[0], lifetime=i[1]).save()

    # Potato = Ingredient(name="Potato", lifetime=30)
    # Potato.save()

    [print(i.name) for i in Ingredient.select()]
