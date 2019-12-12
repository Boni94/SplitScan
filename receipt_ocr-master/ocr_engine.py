try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

#pytesseract.pytesseract.tesseract_cmd = r''

def doOcr(image):
    return pytesseract.image_to_string(image)

#print(pytesseract.image_to_string(Image.open('C:\\Users\\shsg\\Desktop\\summerschool\\project_ocr\\receipt\\grey_1.jpg')))

