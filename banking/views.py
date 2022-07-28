from django.dispatch import receiver
from django.shortcuts import render
from django.http import HttpResponse
from .models import Payment
# Create your views here.

def index(request):
    # return HttpResponse('It is checking')
    if request.method == 'POST':
        sname = request.POST.get('sender_name','')
        semail = request.POST.get('sender_email','')
        amount = request.POST.get('amount_to_pay','')
        rname = request.POST.get('receiver_name','')
        remail = request.POST.get('receiver_email','')

        payment = Payment(sender_name=sname,sender_email=semail,amount=amount,receiver_name=rname,receiver_email = remail)
        payment.save()
        


    payments = Payment.objects.all()
    return render(request,'index.html',{'payments':payments})