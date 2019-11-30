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

    ingredients = [["name", 30],["Avocado", 20],["Bacon", 20],["Bananas", 20],["Bread", 20],["Butter", 20],["Cauliflower", 20],["Chicken", 20],["Cucumber", 20],["Eggs", 20],["Feta cheese", 20],["Frozen Peas", 20],["Garlic", 20],["Kale", 20],["Milk", 20],["Onions", 20],["Pomegranate", 20],["Potatoes", 20],["Red onions", 20],["Salad", 20]]

    for i in ingredients:
        Ingredient(name=i[0], lifetime=i[1]).save()

    # Potato = Ingredient(name="Potato", lifetime=30)
    # Potato.save()

    [print(i.name) for i in Ingredient.select()]
