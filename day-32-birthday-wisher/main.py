import smtplib
import datetime as dt
import random
import pandas

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
# get day
now = dt.datetime.now()
today_tuple = (now.month, now.day)

# my email data
my_email = "bqshina1994@gmail.com"
password = "bqSq9417"
# check birthdays.csv
birthdays_data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(row["month"], row["day"]): row for (index, row) in birthdays_data.iterrows()}


if today_tuple in birthdays_dict:
    # 3. If step 2 is true, pick a random letter from letter templates and
    # replace the [NAME] with the person's actual name from birthdays.csv
    birthday_person = birthdays_dict[today_tuple]
    letter_number = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_number}.txt") as letter:
        letter = letter.read()
        letter_content = letter.replace('[NAME]', birthday_person['name'])
        print(letter_content)
    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Harry Birthday to You!\n\n{letter_content}")
