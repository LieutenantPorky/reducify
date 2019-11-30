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
    Potato = Ingredient(name="Potato", lifetime=30)
    ingredientsDb.create_tables([Ingredient])
    Potato.save()
    [print(i.name) for i in Ingredient.select()]
