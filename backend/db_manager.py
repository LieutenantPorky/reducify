from peewee import *
from playhouse.sqlite_ext import *
import datetime
import json

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

# Create a test JSON to contain a theoretical fridge
testFridge = {"apple":[[1,datetime.datetime(2020, 5, 17).__str__()]]}

class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    id = AutoField()
    fridge = JSONField(default=json.dumps(testFridge))




if __name__ == "__main__":
    db.create_tables([User])



    ingredients = [["Feynman", "pathIntegral"], ["Einstein", "mc2"]]

    for i in ingredients:
        User(username=i[0], password=i[1]).save()

    [print(i.username, i.password, i.id, i.fridge) for i in User.select()]
