from peewee import *
from playhouse.sqlite_ext import *
import datetime
import json
from Recipes import getIngredients, getRecipes

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
testFridge = {"onions":[[1,datetime.date(2020, 5, 17).__str__()]]}

class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    id = AutoField()
    fridge = JSONField(default=json.dumps(testFridge))

    def getFridge(self):
        fridge = json.loads(self.fridge)
        output = []

        for key, value in fridge.items():
            for element in value:
                output.append({"item":key, "number":element[0], "date":element[1]})

        return json.dumps({"data":output})

    def updateFridge(self, items):
        print("updating fridge \n")
        print(items)
        oldFridge = json.loads(self.fridge)
        print(oldFridge)
        for item in items:
            print(item)
            print('\n')
            try:
                sell_by = str(datetime.date.today() + datetime.timedelta(days=Ingredient.get(name=item).lifetime))
            except:
                sell_by = str(datetime.date.today() + datetime.timedelta(days=20))
            if not (item in oldFridge):
                oldFridge[item]=[[1,sell_by]]
            else:
                line = oldFridge[item]
                print(line)

                if len(line)>0 and line[-1][1]==sell_by:
                    line[-1][0] += 1
                else:
                    line.append([1,sell_by])

                oldFridge[item] = line

            self.fridge = json.dumps(oldFridge)
            self.save()

    def foodList(self):
        fridge = json.loads(self.fridge)
        return [i for i in fridge]

    def removeThroughRecipe(self, recipe):
        ingredients = getIngredients(recipe)
        oldFridge = json.loads(self.fridge)
        for i in ingredients:
            if i in oldFridge:
                oldFridge[i][0][0] -=1
                if oldFridge[i][0][0] <= 0:
                    del oldFridge[i][0]

        self.fridge = json.dumps(oldFridge)
        self.save()


def getShared(limit=3):
    collectable = []
    for user in User.select():
        items = json.loads(user.getFridge())["data"]
        for item in items:
            itemSellby = [int(i) for i in item["date"].split('-')]
            if datetime.date(itemSellby[0],itemSellby[1],itemSellby[2]) - datetime.date.today() < datetime.timedelta(days=limit):
                collectable.append({"item":item["item"], "username":user.username})

    return collectable



if __name__ == "__main__":

    for usr in User.select():
        print("username: ", usr.username)
        print(getRecipes(usr.foodList()))
    # db.create_tables([User])
    #
    # ingredients = [["Feynman", "pathIntegral"], ["Einstein", "mc2"]]
    #
    # for i in ingredients:
    #     User(username=i[0], password=i[1]).save()
    #
    # [print(i.username, i.password, i.id, i.fridge) for i in User.select()]
    #
    # [print(i.name, " ", str(i.lifetime)) for i in Ingredient.select()]
    # testUser = User.get(username="Einstein")
    #
    # print (testUser.getFridge())
    # testUser.updateFridge(["chicken", "salad", "red onions", "cucumbers", "pommegranate", "salad", "avocado", "feta cheese"])

    for usr in User.select():
        print("User: " + usr.username)
        print("Password: " + usr.password)
        print("id: " + str(usr.id))
        print(usr.getFridge())
        print("\n ####### \n")
