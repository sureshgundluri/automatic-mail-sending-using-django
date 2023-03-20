from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def Registration(request):
    UF=Userfrom()
    PF=Profileform()
    d={'UF':UF,'PF':PF}
    if request.method=='POST' and request.FILES:
        ufd=Userfrom(request.POST)
        pfd=Profileform(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            UFD=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            UFD.set_password(password)
            UFD.save()


            PFD=pfd.save(commit=False)
            PFD.profile_user=UFD
            PFD.save()
            send_mail('Registration','thankyou for registration',from_email='sureshgundluri75@gmail.com',recipient_list=[UFD.email,'sanvi799515@gmail.com'],fail_silently=False)

            return HttpResponse ('registration is done successfully')
        return HttpResponse('data is invlid')

        
    return render(request,'Registration.html',d)