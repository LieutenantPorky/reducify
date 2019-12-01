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

    ingredients = [["name", 30],["avocado", 5],["bacon", 14],["bananas", 7],["bread", 7],["butter", 270],["cauliflower", 14],["chicken", 2],["cucumbers", 7],["egg", 35],["feta cheese", 5],["frozen peas", 365],["garlic", 150],["kale", 7],["milk", 7],["onions", 60],["pomegranate", 60],["potatoes", 35],["red onions", 60],["salad", 5]]

    for i in ingredients:
        Ingredient(name=i[0], lifetime=i[1]).save()

    # Potato = Ingredient(name="Potato", lifetime=30)
    # Potato.save()

    [print(i.name) for i in Ingredient.select()]
