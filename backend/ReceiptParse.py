import cv2
import pytesseract
from PIL import Image

path="test_receipt.jpg"

# Open the image
image = cv2.imread(path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#do some preprocessing
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
gray = cv2.medianBlur(gray, 3)

pil_img = Image.fromarray(gray)

#print(pytesseract.image_to_string(pil_img))
newString = pytesseract.image_to_string(Image.open("test_receipt.jpg"))
realNew = newString.lower()
print(realNew)

from receipt_parse import filter

import re

wordList = re.sub ("[^\w]"," ",realNew).split()

if __name__ == "__main__":
    input = allIngredients #allIngredients refers to the database containing all ingredients that are used in recipes
    ingredients = [i for i in [filter(i,wordList,70) for i in input] if i] #ingredients in fridge
    print(ingredients)
