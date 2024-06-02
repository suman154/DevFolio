from django.shortcuts import render, redirect
from .forms import ContactMessageForm
from .models import BlogPost
from django.shortcuts import render, get_object_or_404
# Create your views here.
def home(request):
    return render(request, 'base/index.html')



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


