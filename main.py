# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime as dt
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

print("EMAIL:", MY_EMAIL)
print("PASSWORD:", MY_PASSWORD)

#-------------find today's date and month-------------#
today =dt.now()
today_tuple = (today.month,today.day)
print(today_tuple)

#-------------check if today' date and moth matches with birthday.csv records-------------#

birthday_data_frame = pandas.read_csv("birthdays.csv")
print(birthday_data_frame)

birthday_data_dict =birthday_data_frame.to_dict(orient="records")
print(birthday_data_dict)

for person in birthday_data_dict :
	if person["month"] == today_tuple[0] and person["day"] ==today_tuple[1]:
		print(f"Today is {person['name']}'s birthday!")
		filepath = f"letter_template/letter_{random.randint(1,3)}.txt"
		print(filepath)

		with open (filepath) as letter_file :
			content = letter_file.read()
			content = content.replace("[NAME]",person["name"])

#-----------------send email to the person--------------------------#

		with smtplib.SMTP("smtp.gmail.com",587) as connection:
			connection.starttls()
			connection.login(MY_EMAIL,MY_PASSWORD)
			connection.sendmail(from_addr=MY_EMAIL,to_addrs = person["email"],msg=f"Subject:Happy Birthday!\n\n{content}")
