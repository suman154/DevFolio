from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('experience/', views.experience, name='experience'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('price/', views.price, name='price'),
    path('review/', views.review, name='review'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success_view, name='contact_success'),
    path('blog/', views.blog_view, name='blog'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


