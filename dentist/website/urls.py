from django.urls import path
from . import views
from .views import send_mail

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('doctors.html', views.doctors, name="doctors"),
    path('send-mail/', send_mail, name='send_email')
]