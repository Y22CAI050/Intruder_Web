import yagmail

def send_email():
    sender = "shaikasma8275@gmail.com"
    password = "Asma8275@"
    receiver = "shaikasma8275@gmail.com"

    yag = yagmail.SMTP(sender, password)
    yag.send(
        to=receiver,
        subject="INTRUDER ALERT!",
        contents="Motion detected. See attached image.",
        attachments="intruder.jpg"
    )
