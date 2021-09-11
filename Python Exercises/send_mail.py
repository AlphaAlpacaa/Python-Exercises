import smtplib
content = "Hi"
mail = smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
mail.login("gmail@gmail.com","password")
mail.sendmail("gmail@gmail.com","other_gmail@gmail.com",content)