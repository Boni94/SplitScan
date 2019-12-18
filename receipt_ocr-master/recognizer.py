#first of all, the necessary functions need to be imported into this main code from the libraries
import ocr_engine
import coop_recognizer
import migros_recognizer
import csv_writer

try:
    from PIL import Image
except ImportError:
    import Image
import os

#the data depends on the store of which the receipt is from and therefore we need an if/elif/else differentiation
def recognize(text):
    name = ""
    total = "notFound"
    date = None
    category = ""
#if it's a Coop receipt the following data will be read from the receipt and labeled as the variables below
    if(coop_recognizer.is_coop(text)):
        name = "Coop"
        total =  coop_recognizer.get_total(text)
        date = coop_recognizer.get_date(text)
        category = "Groceries"
#if it's a Migros receipt the following data will be read from the receipt and labeled as the variables below  
    elif(migros_recognizer.is_migros(text)):
        name = "Migros"
        total =  migros_recognizer.get_total(text)
        date = migros_recognizer.get_date(text)
        category = "Groceries"
    else:
        name = "Not implemented"   
#in either case we want the following informations to be returned from all receipts  
    return [name, total, date, category]

#we use the os.listdir() to manipulate/use the paths contained in the directory "a_dirname" and put them in a list
def get_filenames(a_dirname):
  list_of_files = os.listdir(a_dirname)
  all_files = []
  for filename in list_of_files:
    full_path = os.path.join(a_dirname,filename)
    if os.path.isdir(full_path): # if the file is a dir we skip it
      pass
 #all the files (besides from dir will be added to the list "all_files")
    else:
      all_files.append(full_path)
  return all_files

#this function applies the optical character recognition tool to all receipts
#and adds the ones that were recognizable to the list "recognized_list"
def ocr_all_images(folder_name):
    img_list = get_filenames(folder_name)
    recognized_list = []
    print(img_list)
    for each_img in img_list:
      image = Image.open(each_img)
      text = ocr_engine.doOcr(image)
      recognized_list.append(recognize(text))
    return recognized_list

#this function applies the optical character recognition tool to single receipts
#and adds the ones that were recognizable to the list "recognized_list" 
def ocr_single_image(pic):
    img_list = [pic]
    recognized_list = []
    print(img_list)
    for each_img in img_list:
      image = Image.open(each_img)
      text = ocr_engine.doOcr(image)
      recognized_list.append(recognize(text))
    return recognized_list



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


#the last statement we need is: if __name__ == "__main__" which makes the underlying function "run()"
#only being executed if we're in the home script. This is crucial since we imported several functions from 
#our libraries into the home script. It prevents the imported code from beeing run because the 
#interpreter labels the imported code as __name__ but not as __main__
if __name__ == "__main__":
  run()

