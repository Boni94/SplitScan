import datetime
import re


def is_migros(text):
    if "migros" in text.lower():
        return True
    else:
        return False

def get_total(text):
    try:
        total = re.search('(TOTAL *\d*\.\d*|CHF *\d*\.\d*)', text).group(1)
        total = total.split()[1]
        return total
    except:
        return "Not found"


def find_date(text):
    for line in text:
        match = re.search('\d{2}.\d{2}.\d{4}', text)        
        date = str(datetime.datetime.strptime(match.group(), '%d.%m.%Y').date())
        return date

def get_date(text):
    if find_date(text):
        return find_date(text)
    else:
        print("Date not found. Please enter the date manually")
        date = str(input("Enter year ") + "-" + input("Enter month ") + "-" + input("Enter day "))
        return date    
