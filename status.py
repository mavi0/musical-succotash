import os, errno, glob, sys, smtplib, ssl
import schedule, subprocess, logging


logging.basicConfig(format='[%(levelname)s] %(asctime)s %(message)s ',filename='status.log',level=logging.INFO)

def mail(content):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "a09.athena@gmail.com"
    receiver_email = "ellie@mavieson.co.uk"
    password = "@oMr^&pcS$rhCM85O#PaG7c&gT$Z2oWGgNsqRc#%"
    message = content

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def main():
    if b'State: running' in subprocess.check_output(["systemctl", "status"]):
        logging.info("Running")
    else:
        logging.warning("Degraded")
        mail("""\
            Athena Degraded

            A service on Athena has failed, action may be required""")
main()
