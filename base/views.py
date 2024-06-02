from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request, "base/index.html")



from django.shortcuts import render, redirect
from .forms import ContactMessageForm
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactMessageForm()
    
    return render(request, 'base/index.html.html', {'form': form})

def contact_success_view(request):
    return render(request, 'base/contact_success.html')
