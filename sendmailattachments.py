import smtplib
import base64
sender = 'yourgmail@gmail.com'
receiver = 'receiveremail@gmail.com'
file = "/path/filename.extension"
file_read = open(file, "rb")
file_content = file_read.read()
encoded_content = base64.b64encode(file_content) 
marker = "AUNIQUEMARKER"
body = """
I learned to send email using Python programming on programminghub tutorial.
"""
one = """From: From Programminghub <yourgmail@gmail.com>
To: To Learner <receiveremail@gmail.com>
Subject: Sending Email using Python
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)
two = """Content-Type: text/plain
Content-Transfer-Encoding:8bit
%s
--%s
""" % (body, marker)
three = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; file=%s
%s
--%s--
""" % (file, file, encoded_content, marker)
msg = one + two + three
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, "Sender_Password_Here")
server.sendmail(sender, receiver, msg)
server.quit()
