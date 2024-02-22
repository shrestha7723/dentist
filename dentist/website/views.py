from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request, "home.html", {})

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        # send email
        send_mail(
            "message from "+ name, # subject
            message, # message
            email, # from email
            ["nshresthan@gmail.com"],# to email

        )

        return render(request, "contact.html", {'name': name})

    return render(request, "contact.html", {})

def doctors(request):
    return render(request, "doctors.html", {})