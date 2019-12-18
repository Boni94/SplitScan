#we use tempfile to use temporary files to store data in our python program
import tempfile
#cv2 as our open source computer vison tool to be able to "read" the data
#on the pictures in the first place
import cv2
import numpy as np
#np (NumPy) for the multi-dimensional data on the receipts
#to sort and extract the exact data we need

def preprocess(image):
    return  image


# Scaling of image to have the pictures of the receipts
# in the same usable format
def set_image_dpi(file_path):
    im = Image.open(file_path)
    length_x, width_y = im.size
    factor = min(1, float(1024.0 / length_x))
    size = int(factor * length_x), int(factor * width_y)
#use of Antialias to make lines smoother and better readable
    im_resized = im.resize(size, Image.ANTIALIAS)
    temp_file = tempfile.NamedTemporaryFile(delete=False,   suffix='.png')
    temp_filename = temp_file.name
    im_resized.save(temp_filename, dpi=(300, 300))
    return temp_filename

# Noise Removal or Denoise to make the picture smoother and less blurry
def remove_noise_and_smooth(file_name):
    img = cv2.imread(file_name, 0)
#use of adaptiveThreshold(src= input, dst= output, maxValue, adaptiveMethod, thresholdType, blockSize, C)
#to calculate the thresholds for smaller regions within the picture
    filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 41)
    kernel = np.ones((1, 1), np.uint8)
    opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    or_image = cv2.bitwise_or(img, closing)
    return or_image


