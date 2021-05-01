#pip install pdfreader
import subprocess
subprocess.call('./setup.sh')

import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer
import smtplib
#import subprocess
from email.message import EmailMessage
import schedule
import time

fd = open("sherlock.pdf", "rb")
viewer = SimplePDFViewer(fd)

print(fd)

viewer.navigate(6)
viewer.render()
page_1_canvas = viewer.canvas

page_1_text = viewer.canvas.strings

final_text = ' '.join(page_1_text)
print(final_text)

msg = EmailMessage()
msg['Subject'] = 'Sherlock Day 1'
msg['From'] = 'pytest8000@gmail.com' 
msg['To'] = 'pytest8000@gmail.com' 
msg.set_content(final_text)


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('pytest8000@gmail.com', 'mvxx vdyw dzcs xrfk') 

    smtp.send_message(msg)