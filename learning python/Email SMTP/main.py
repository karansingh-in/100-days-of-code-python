import smtplib

my_email = '<my email address>'
password = '<app password>'
connection = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10)
# connection.starttls() # start TLS
try:
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs='<sender email>', msg='Subject:testing phase 1\n\nThis is the body of the mail thanks')
    print("Email sent successfully!")
    
except Exception as e:
    print(f"Error: {e}")
    
connection.close()


