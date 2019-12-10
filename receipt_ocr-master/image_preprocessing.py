import tempfile
import cv2
import np

def preprocess(image):
    return  image



# Scaling of image
def set_image_dpi(file_path):
    im = Image.open(file_path)
    length_x, width_y = im.size
    factor = min(1, float(1024.0 / length_x))
    size = int(factor * length_x), int(factor * width_y)
    im_resized = im.resize(size, Image.ANTIALIAS)
    temp_file = tempfile.NamedTemporaryFile(delete=False,   suffix='.png')
    temp_filename = temp_file.name
    im_resized.save(temp_filename, dpi=(300, 300))
    return temp_filename


# Noise Removal or Denoise
def remove_noise_and_smooth(file_name):
    img = cv2.imread(file_name, 0)
    filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 41)
    kernel = np.ones((1, 1), np.uint8)
    opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
   # img = image_smoothing(img)
    or_image = cv2.bitwise_or(img, closing)
    return or_image

#dpi_image = set_image_dpi('C:\\Users\\shsg\\Desktop\\summerschool\\project_ocr\\receipt\\grey_1.jpg')
#smooth_image = remove_noise_and_smooth(dpi_image)