from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import contact_view, contact_success_view
from .views import blog_view, blog_detail_view
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success_view, name='contact_success'),
    path('blog/', blog_view, name='blog'),
    path('blog/<int:id>/', blog_detail_view, name='blog_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




