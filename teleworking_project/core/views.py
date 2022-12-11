import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import os
import json

from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

smtpHost = "smtp.gmail.com"
smtpPort = 587
mailUname = "remotely.leads@gmail.com"
mailPwd = "zqnlzswcmwjbjnbz"

#recepientsMailList = [mailUname, "shayonbanerjee123@gmail.com", "kerthanan20@gmail.com"]
recepientsMailList = [mailUname, "shayonbanerjee123@gmail.com"]

@api_view(('POST',))
@csrf_exempt
@permission_classes([AllowAny])
def contact_us(request):
    """ Contact us request """
    form_request = json.loads(request.body)
    name = form_request["name"]
    email = form_request["email"]
    message = form_request["message"]

    print("SHAYOB_DEBUG - name: " + name)
    print("SHAYOB_DEBUG - email: " + email)
    print("SHAYOB_DEBUG - message: " + message)

    email_title = "Remotely - " + email + " Inquiry"
    email_body = "Sender Name: " + name + "<br/>" + message

    msg = MIMEMultipart()
    msg['From'] = mailUname
    msg['To'] = ",".join(recepientsMailList)
    msg['Subject'] = email_title
    msg.attach(MIMEText(email_body, 'html'))

    # Send message using smtpplib
    s = smtplib.SMTP(smtpHost, smtpPort)
    s.starttls()
    s.login(mailUname, mailPwd)
    msgText = msg.as_string()
    sendErrs = s.sendmail(mailUname, recepientsMailList, msgText)
    s.quit()

    if not len(sendErrs.keys()) == 0:
        raise Exception("Error occured while sending email", sendErrs)

    return Response(status=status.HTTP_200_OK)