from django.core.mail import EmailMessage, get_connection
# from django.conf import settings

import settings

# settings = settings.configure()
def send_email():  
#    if request.method == "POST": 
    with get_connection(  
        host=settings.EMAIL_HOST, 
    port=settings.EMAIL_PORT,  
    username=settings.EMAIL_HOST_USER, 
    password=settings.EMAIL_HOST_PASSWORD, 
    use_tls=settings.EMAIL_USE_TLS  
    ) as connection:  
        subject = "test mail" # subject = request.POST.get("subject")  
        email_from = settings.EMAIL_HOST_USER  
        recipient_list =  ["nshresthan@gmail.com", ]   #[request.POST.get("email"), ]  
        message = "this is test message"#request.POST.get("message")  
        EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()  
    
    print("message sent.")
#    return render(request, 'home.html')
    
send_email()