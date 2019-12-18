#we use the following libraries
#datetime to locate the time of purchase on the receipts
import datetime
#re = regular expression to locate other specific characters (the price)
import re

#as the various receipts have different structures we first need to know
#from which store a specific receipt is. Therefore we define functions for the
#various stores so that the ocr can differentiate them
#the following code is specified for receipts from Coop
def is_coop(text):
    if "coop" in text.lower():
        return True
    else:
        return False

#(see picture of a coop receipt)
#the following function lets us separate the information on the line with the
#total price of the purchase

#re.search locates the line with the total amount on it
#(TOTAL *\d*\.\d*|CHF: *\d*\.\d*) defines the different aspects where we need to split the infos
#in order to get the numbers (-> the price)
def get_total(text):
    try:
        total = re.search('(TOTAL *\d*\.\d*|CHF: *\d*\.\d*)', text).group(1)
        total = total.split()[1]
        return total
    except:
        return "Not found"

#to receive the date of purchase from the receipt
#using re.search again but this time to localize the formate "day/month/year"
#datetime.strprime() reads the data and compiles it into the "d/m/y" format
def find_date(text):
    for line in text:
        match = re.search('\d{2}.\d{2}.\d{4}', text)        
        date = str(datetime.datetime.strptime(match.group(), '%d.%m.%Y').date())
        return date

#to make sure we get a date in the end we either pull it directly from the function above
#or let it be typed in manually in case the find_date function cannot localize the date
def get_date(text):
    if find_date(text):
        return find_date(text)
    else:
        print("Date not found. Please enter the date manually")
        date = str(input("Enter year ") + "-" + input("Enter month ") + "-" + input("Enter day "))
        return date    

        