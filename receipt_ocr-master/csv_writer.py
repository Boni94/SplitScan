import csv

def write(my_path,recognized_list):
    for each_list in recognized_list:
        shopping_records = open(my_path, "a", newline="")
        with shopping_records:
            writer = csv.writer(shopping_records)
            writer.writerow(each_list)
        shopping_records.close()


import gspread
from oauth2client.service_account import ServiceAccountCredentials

def write2(my_path,recognized_list):
    for each_list in recognized_list:
        #shopping_records = open(my_path, "a", newline="")
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)
        sheet = client.open('Shopping List').sheet1
        sheet.insert_row(each_list)
        list_of_hashes = sheet.get_all_records()
        print(list_of_hashes)

print("Writing complete")

'''def write(file, value_list):
    print("write values into csv file")

["02.02.2020","groceries","23.20"]
shopping_records = open("C:\\Users\\dinti\\Documents\\Studium\\Master\\Summerschool\\Python Files\\receipt_ocr\\" + "shopping_records.csv", "a", newline="")

import csv

my_data = ["02.02.2020","groceries","23.20"]

def write(my_data,my_path):
    shopping_records = open(my_path, "a", newline="")
    with shopping_records:
        writer = csv.writer(shopping_records)
        writer.writerow(my_data)
    shopping_records.close()

write(my_data)
'''

