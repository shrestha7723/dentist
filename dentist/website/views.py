from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

from django.core.mail import get_connection
from django.core.mail.message import EmailMessage

# Create your views here.
def home(request):
    return render(request, "home.html", {})

connection = get_connection(use_tls=True, host='smtp.gmail.com', port=587,username="ns77850617@gmail.com", password="whoi axcx gfuv rbsm")
def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        if name:
            print(f"Getting message from {name}")

        # send email
        EmailMessage(subject=subject, body=message, from_email="ns77850617@gmail.com", to=[email], connection=connection).send()
        # send_mail(
        #     "message from "+ name, # subject
        #     message, # message
        #     email, # from email
        #     ["nshresthan@gmail.com"],# to email
        # )

        return render(request, "contact.html", {'name': name})

    return render(request, "contact.html", {})

def doctors(request):
    return render(request, "doctors.html", {})




def send_mail(request):
    connection = get_connection(use_tls=True, host='smtp.gmail.com', port=587,username="ns77850617@gmail.com", password="whoi axcx gfuv rbsm")
    

    subject = 'Welcome to My Site'
    message = 'Thank you for creating an account!'
    from_email = 'nshresthan@gmail.com'
    recipient_list = ['nshresthan@gmail.com']
    EmailMessage('test', 'test', "ns77850617@gmail.com", ["ns77850617@gmail.com"], connection=connection).send()
    # send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)
    return HttpResponse("Message sent.")