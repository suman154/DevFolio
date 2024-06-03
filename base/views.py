from django.shortcuts import render, redirect
from .forms import ContactMessageForm
from .models import BlogPost
from .models import Pricing
from django.conf import settings
from django.shortcuts import render, get_object_or_404
# Create your views here.
def home(request):
    blog_posts = BlogPost.objects.all().order_by('-date_posted')
    return render(request, 'base/index.html', {'blog_posts': blog_posts})


def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactMessageForm()
    
    return render(request, 'base/index.html', {'form': form})

def contact_success_view(request):
    return render(request, 'base/contact_success.html')
        

def blog_view(request):
    blog_posts = BlogPost.objects.all().order_by('-date_posted')
    return render(request, 'base/index.html', {'blog_posts': blog_posts})


def blog_detail_view(request, id):
    blog_post = get_object_or_404(BlogPost, id=id)
    return render(request, 'base/blog_detail.html', {'blog_post': blog_post})




def order_view(request, plan_id):
    plan = get_object_or_404(Pricing, id=plan_id)
    return render(request, 'base/order.html', {'plan': plan})

def esewa_payment(request):
    if request.method == 'POST':
        plan_id = request.POST.get('plan_id')
        plan = get_object_or_404(Pricing, id=plan_id)
        amount = plan.price

        esewa_merchant_code = 'YOUR_MERCHANT_CODE'
        return_url = request.build_absolute_uri('/esewa_success/')
        cancel_url = request.build_absolute_uri('/esewa_failure/')

        context = {
            'plan': plan,
            'amount': amount,
            'esewa_merchant_code': esewa_merchant_code,
            'return_url': return_url,
            'cancel_url': cancel_url,
        }
        return render(request, 'base/esewa_payment.html', context)
    return redirect('home')

def esewa_success(request):
    # Handle the success callback from eSewa
    return render(request, 'base/esewa_success.html')

def esewa_failure(request):
    # Handle the failure callback from eSewa
    return render(request, 'base/esewa_failure.html')
