from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import ContactForm
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request, "base/index.html")



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                send_mail(
                    form.cleaned_data['subject'],
                    form.cleaned_data['message'],
                    form.cleaned_data['email'],
                    ['sumanbhatta735@gmail.com'],  # Change this to your recipient email
                    fail_silently=False,
                )
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'error_message': str(e)}, status=500)
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = ContactForm()
    return render(request, "base/contact.html", {'form': form})
