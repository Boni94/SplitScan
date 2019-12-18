#We use pytesseract as our optical character recognition tool in order to read the scanned receipts
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


#in order to further use the data from the scanned receipts we need the data to be 
#changed into a string (instead of the picture)
def doOcr(image):
    return pytesseract.image_to_string(image)



