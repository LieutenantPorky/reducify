import cv2
import pytesseract
from PIL import Image


path="test_receipt.jpg"

# Open the image
image = cv2.imread(path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#do some preprocessing
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#gray = cv2.medianBlur(gray, 3)

pil_img = Image.fromarray(gray)

print(pytesseract.image_to_string(pil_img))
