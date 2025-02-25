##################### Extra Hard Starting Project ######################
import random
import smtplib

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
################# read birthdays.csv
df = pandas.read_csv('birthdays.csv')
print(df)

print( {row['name']:{'email':row['email'],'date':row['day'],'month':row['month'] } for index, row in df.iterrows()})

import datetime
today = datetime.datetime.today().date()
DAY = today.day
MONTH = today.month

############################ SMTP credentials ############################
my_email = "python60daysofcode@gmail.com"
password = "oplvlvifuagvukjp"


############# DATAFRAME #############
birthday_data = df[(df['month'] == MONTH) & (df['day'] == DAY)]
names = birthday_data['name'].tolist()
email = birthday_data['email'].tolist()



print(names,email)

for n in range(len(names)):
    with open(f'./letter_templates/letter_{random.randint(1,3)}.txt') as file:
        start_letter = file.read()
        start_letter = start_letter.replace('[NAME]',names[n])


    ################send email##########################
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=f'{email[n]}',
                            msg=f"Subject:Happy Birthday!!\n\n {start_letter}")
        print("Mail Sent")