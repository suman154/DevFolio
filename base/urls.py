from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success_view, name='contact_success'),
    path('blog/', views.blog_view, name='blog'),
    path('blog/<int:id>/', views.blog_detail_view, name='blog_detail'),
    path('order/<int:plan_id>/', views.order_view, name='order'),
    path('esewa_payment/', views.esewa_payment, name='esewa_payment'),
    path('esewa_success/', views.esewa_success, name='esewa_success'),
    path('esewa_failure/', views.esewa_failure, name='esewa_failure'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


