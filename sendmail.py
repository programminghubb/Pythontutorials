import smtplib
sender = "yourgamil@gmail.com"
receiver = "receiversemail@gmail.com"
msg = """From: From Programminghub <yourgmail@gmail.com>
To: To Learner <receiversemail@gmail.com>
Subject: Sending Email using Python
I learned to send email using Python programming on programminghub tutorial.
"""
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender, "Sender_gmail_password")
server.sendmail(sender, receiver, msg)
server.quit()
