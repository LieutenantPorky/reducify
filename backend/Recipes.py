
potatoTortilla = ["potatoes", "eggs", "onions"] #salt, pepper

breadSoup = ["bread", "onions","frozen peas"] #salt, pepper, stock cube, oil

cauliflowerSoup = ["onions", "garlic", "cauliflower", "kale", "bacon", "milk"] #stock cube, salt, pepper, oil

chickenSalad = ["chicken", "salad", "red onions", "cucumbers", "pommegranate", "salad", "avocado", "feta cheese"] # salt, pepper, oil/butter

bananaPancakes = ["milk", "butter", "eggs", "bananas"] # flour, baking powder, salt

frenchToast = ["bread", "eggs", "milk"] # oil, sugar, salt

breadPizza = ["bread", "tomatoes", "cheese"] # pepper, herbs


# [recipe, name of recipe, time, dietaryRestrictions]
recipes = [[bananaPancakes, "Banana Pancakes", 15, "Ve"], [breadSoup, "Bread Soup", 30, "V"],[cauliflowerSoup, "Cauliflower Soup", 30, "G"] , [chickenSalad, "Chicken Salad", 15, "G"], [frenchToast, "French Toast", 10, "Ve"], [potatoTortilla, "Potato Tortilla", 30, "Ve"], [breadPizza,"Bread Pizza", 15, "Ve" ]]

def getIngredients(recipe):
    for i in recipes:
        if i[1].lower() == recipe.lower():
            return i[0]
    return []

def getRecipes(ingredients):
    recipesOut = []
    for i in range(len(recipes)):
        currentRecipe = recipes[i][0]

        for x in range(len(currentRecipe)):
            if currentRecipe[x] not in ingredients:
                break
        else:
            recipesOut.append({"name":recipes[i][1], "ingredients":recipes[i][0]})
    return recipesOut

if __name__=="__main__":
    print(getRecipes(["milk", "butter", "eggs", "bananas", "milk", "butter", "bread", "bananas"]))
    print(getIngredients("breadPizza"))
