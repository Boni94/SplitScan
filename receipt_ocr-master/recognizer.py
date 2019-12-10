import ocr_engine
import coop_recognizer
import migros_recognizer
import csv_writer
# import image_preprocessing
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
        name = "Coop"
        total =  coop_recognizer.get_total(text)
        date = coop_recognizer.get_date(text)
        category = "Groceries"
    elif(migros_recognizer.is_migros(text)):
        name = "Migros"
        total =  migros_recognizer.get_total(text)
        date = migros_recognizer.get_date(text)
        category = "Groceries"
    else:
        name = "Not implemented"   
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
  
def ocr_single_image(pic):
    img_list = [pic]
    recognized_list = []
    print(img_list)
    for each_img in img_list:
      image = Image.open(each_img)
      text = ocr_engine.doOcr(image)
      recognized_list.append(recognize(text))
    return recognized_list

#image = Image.open('C:\\Users\\shsg\\Desktop\\summerschool\\project_ocr\\receipt\\img_3412.jpg')
#image = image_preprocessing.preprocess(image)
#text = ocr_engine.doOcr(image)
#recognized_list = recognize(text)
#csv_writer.write('C:\\Users\\shsg\\Desktop\\summerschool\\project_ocr\\result.csv', recognized_list)
#print(recognized_list)

def run():
  working_directory = os.path.dirname(os.path.realpath(__file__))
  img_path = os.path.join(working_directory, "receipt")
  recognized_list = ocr_all_images(img_path)
  print(working_directory, img_path, recognized_list)
  csv_writer.write2(os.path.join(working_directory, 'result.csv'), recognized_list)
  csv_writer.write(os.path.join(working_directory, 'result.csv'), recognized_list)

def run_single(filename):
  working_directory = os.path.dirname(os.path.realpath(__file__))
  img_path = os.path.join(working_directory, "receipt")
  full_img_path = os.path.join(img_path, filename)
  recognized_list = ocr_single_image(full_img_path)
  print(working_directory, img_path, recognized_list)
  csv_writer.write2(os.path.join(working_directory, 'result.csv'), recognized_list)
  csv_writer.write(os.path.join(working_directory, 'result.csv'), recognized_list)



if __name__ == "__main__":
  run()