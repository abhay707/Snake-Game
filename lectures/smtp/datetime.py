import datetime as dt
import random
import smtplib

now = dt.now()
# year = now.year
# month = now.month
week_day = now.weekday()

# date_of_brith = datetime(year=2004, month=10, day=7, hour=10)
# print(date_of_brith)

my_email = "mypython92@gmail.com"
password = "jklfpaefxiaagwqk"

if week_day == 0:

    with open("quotes.txt") as data:
        read = data.readlines()
        quote = random.choice(read)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="abhx1437@gmail.com", msg=f"Subject:Today's Motivational quote\n\n{quote}")
