
import random
import datetime as dt
import smtplib
my_email = "selvam1921992@gmail.com"
password = "ucepdltexjywaons"
today_month = dt.datetime.now().month
today_day = dt.datetime.now().day
today = (today_month,today_day)

import pandas
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"],data_row["day"]):data_row for (index, data_row) in data.iterrows()}


if today in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open (file_path) as birthday_letter:
        contents = birthday_letter.read()
        contents = contents.replace("[NAME]",birthdays_dict[today]["name"])

    with smtplib.SMTP(host="smtp.gmail.com",port=587) as connection:
        connection.starttls()



        connection.login(user= my_email,password = password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthdays_dict[today]["email"],
            msg = f"Subject: Happy Birthday Wishes\n\n{contents}"

        )



# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



