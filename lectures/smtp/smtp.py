import smtplib

my_email = "mypython92@gmail.com"
password = "jklfpaefxiaagwqk"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="abhx75@yahoo.com",
                        msg="Subject:Hello\n\nThis is the body of my email")
