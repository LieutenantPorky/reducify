import cv2
import pytesseract
from PIL import Image
from receipt_parse import filter
import re
from peewee import *
from db_manager import Ingredient
from io import StringIO
import numpy as np
import base64

path="test_receipt.jpg"

allIngredients = [ingredient.name for ingredient in Ingredient.select()]



def receiptToIngredients(imageStream):
    # Open the image using PIL

    pilImage = Image.open(StringIO(imageStream.read()))

    image = np.array(pilImage)
    print(image.shape())
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #do some preprocessing
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray = cv2.medianBlur(gray, 3)

    pil_img = Image.fromarray(gray)

    #print(pytesseract.image_to_string(pil_img))
    newString = pytesseract.image_to_string(Image.open("test_receipt.jpg"))
    realNew = newString.lower()

    wordList = re.sub ("[^\w]"," ",realNew).split()
    allIngredients #allIngredients refers to the database containing all ingredients that are used in recipes
    ingredients = [i for i in [filter(i,wordList,70) for i in allIngredients] if i] #ingredients in fridge
    return ingredients


if __name__=="__main__":
    print(receiptToIngredients(open(path, 'rb')))
