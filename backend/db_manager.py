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
testFridge = {"apple":[[1,datetime.date(2020, 5, 17).__str__()]]}

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

        return json.dumps(output)

    def updateFridge(self, items):

        oldFridge = json.loads(self.fridge)
        for item in items:
            sell_by = str(datetime.date.today() + datetime.timedelta(days=Ingredient.get(name=item).lifetime))
            if not item in oldFridge:
                oldFridge[item]=[[1,sell_by]]
            else:
                line = oldFridge[item]
                print(line)
                if line[-1][1]==sell_by:
                    line[-1][0] += 1
                else:
                    line.append([1,sell_by])

                oldFridge[item] = line

            self.fridge = json.dumps(oldFridge)
            self.save()




if __name__ == "__main__":
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

    testUser = User.get(username="Feynman")
    print (json.loads(testUser.fridge))

    testUser.updateFridge(["carrots"])


    print (testUser.getFridge())
