#pip install pdfreader
import subprocess
# subprocess.call('./setup.sh')

import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer
import smtplib
#import subprocess
from email.message import EmailMessage
from schedule import every, repeat, run_pending
import time

fd = open("sherlock.pdf", "rb")
viewer = SimplePDFViewer(fd)

print(fd)

@repeat(every(10).seconds)
def send_page():
    page_num = 9
    print("Page num:  " + str(page_num))
    viewer.navigate(int(page_num))
    viewer.render()
    # page_1_canvas = viewer.canvas

    page_1_text = viewer.canvas.strings

    final_text = ' '.join(page_1_text)
    print("-----B4 text print")
    #   print(final_text)

    msg = EmailMessage()
    msg['Subject'] = 'Sherlock Day ' + str(page_num)
    msg['From'] = 'pytest8000@gmail.com' 
    msg['To'] = 'pytest8000@gmail.com' 
    msg.set_content(final_text)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('pytest8000@gmail.com', 'mvxx vdyw dzcs xrfk') 

        smtp.send_message(msg)
    print("----Email sent!-----")
    # page_num = page_num + 1

while True:
    run_pending()
    time.sleep(1)

# j = 9
# schedule.every(20).seconds.do(send_page(j), j)
# print("Hi")