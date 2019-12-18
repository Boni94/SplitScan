#we need csv to read and write tabular data in the spreadsheet
import csv

#the following is needed to manipulate the path of certain data we use
from os.path import join, dirname, realpath

#the following function lists the data of the receipts into a csv-file
#every new object is written on a new row
def write(my_path,recognized_list):
    for each_list in recognized_list:
        shopping_records = open(my_path, "a", newline="")
        with shopping_records:
            writer = csv.writer(shopping_records)
            writer.writerow(each_list)
        shopping_records.close()

#we use gspread to use google spreadsheets to store our data
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#the following function writes the data into the google spreadsheet.
def write2(my_path,recognized_list):
    for each_list in recognized_list:
        #shopping_records = open(my_path, "a", newline="")
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(join(dirname(realpath(__file__)), 'client_secret.json'), scope)
        client = gspread.authorize(creds)
        sheet = client.open('ReceiptsList').sheet1
        sheet.insert_row(each_list)
        list_of_hashes = sheet.get_all_records()
        print(list_of_hashes)



