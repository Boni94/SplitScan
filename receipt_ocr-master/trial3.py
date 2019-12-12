import ocr_engine
import coop_recognizer
import migros_recognizer
import csv_writer
import image_preprocessing
try:
    from PIL import Image
except ImportError:
    import Image
import os

def recognize(text):
    name = ""
    total = "notFound"
    date = None
    category = ""
    if(coop_recognizer.is_coop(text)):
        name = "coop"
        total =  coop_recognizer.get_total(text)
        date = "mydate"#coop_recognizer.get_date(text)
        category = "groceries"
    elif(migros_recognizer.is_migros(text)):
        name = "migros"
        total =  migros_recognizer.get_total(text)
        date = "mydate" #migros_recognizer.get_date(text)
        category = "groceries"
    else:
        name = "not implemented"   
    return [name, total, date, category]


def get_filenames(a_dirname):
  list_of_files = os.listdir(a_dirname)
  all_files = []
  for filename in list_of_files:
    full_path = os.path.join(a_dirname,filename)
    if os.path.isdir(full_path): # if the file is a dir we skip it
      pass
    else:
      all_files.append(full_path)
  return all_files

def ocr_all_images(folder_name):
    img_list = get_filenames(folder_name)
    recognized_list = []
    print(img_list)
    for each_img in img_list:
      image = Image.open(each_img)
      text = ocr_engine.doOcr(image)
      recognized_list.append(recognize(text))
    return recognized_list

image = Image.open('C:\\Users\\SophiaUngerer\\Desktop\\SummerSchool\\receipt_ocr\\receipt\\grey\\grey_3.jpg')
#image = image_preprocessing.preprocess(image)
text = ocr_engine.doOcr(image)
#recognized_list = recognize(text)
#csv_writer.write('C:\\Users\\shsg\\Desktop\\summerschool\\project_ocr\\result.csv', recognized_list)

#print(recognized_list)

# working_directory = dir_path = os.path.dirname(os.path.realpath(__file__))
# img_path = os.path.join(working_directory, "receipt")
# recognized_list = ocr_all_images(img_path)
# csv_writer.write(os.path.join(working_directory, 'result.csv'), recognized_list)

print(text)

