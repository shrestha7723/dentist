import os
from django.conf import settings
from django.core.mail import send_mail

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dentist.settings')

os.environ['DJANGO_SETTINGS_MODULE']= 'dentist.dentist.settings'


subject = 'welcome to GFG world'
message = f'Hi , thank you for registering in geeksforgeeks.'
email_from = "nshresthan@gmail.com" #settings.EMAIL_HOST_USER
recipient_list = ["nshresthan@gmail.com", ]
send_mail( subject, message, email_from, recipient_list )
