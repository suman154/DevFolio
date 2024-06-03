from django.contrib import admin
from .models import ContactMessage
from .models import BlogPost
from .models import Pricing
# Register your models here.
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    list_filter = ('name', 'email') 
    search_fields = ('name', 'email', 'subject')
    ordering = ('-id',)  
    list_display_links = ('name', 'email')
    
admin.site.register(ContactMessage, ContactMessageAdmin)



from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'date_posted', 'comments_count')
    search_fields = ('title', 'content')
    list_filter = ('date_posted', 'category')

admin.site.register(BlogPost, BlogPostAdmin)




class PricingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'disk_space', 'email_accounts', 'support')
    list_filter = ('title', 'price')
    search_fields = ('title', 'support')

admin.site.register(Pricing, PricingAdmin)
