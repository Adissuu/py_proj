import smtplib
import datetime as dt
import pandas


my_email = "pythonanglecode@gmail.com"
password = "hvcppnquacdpfmbe"


today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = "letter.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[Name]", birthday_person["name"])

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday"
                                                                                   f"\n\n{contents}")

