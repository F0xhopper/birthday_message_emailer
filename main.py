##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import pandas
import datetime
import smtplib
import random

my_email = 'sender email'
my_password = 'sender password'

today_date = datetime.datetime.now()
today_month = today_date.month
today_day = today_date.day

birthdays_as_df = pandas.read_csv('birthdays.csv')
birthday_csv = {}
for index, row in birthdays_as_df.iterrows():
    key_tuple = (row['month'], row['day'])  
    value = row 
    birthday_csv[key_tuple] = value

if (today_month,today_day) in birthday_csv:
    persons_name = birthday_csv[(today_month,today_day)]['name']
    persons_email = birthday_csv[(today_month,today_day)]['email']
    letter_path = random.choice(['letter_templates/letter_1.txt','letter_templates/letter_2.txt','letter_templates/letter_3.txt'])
    with open(letter_path) as letter:
        to_send = letter.read().replace('[NAME]',persons_name)



    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,to_addrs=persons_email,msg=f'Subject:Happy Birthday\n\n{to_send}')
      
