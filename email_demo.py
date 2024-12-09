import yagmail

yag = yagmail.SMTP(
    user="nuges1.62@gmail.com", password="Morire222#", host="smtp.gmail.com"
)
yag.send(to="nuges1.62@gmail.com", subject="From yag", contents="kkkk")
print("Email sent successfully!")
