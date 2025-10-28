from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Blog

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'bio', 'profile_picture', 
                  'linkedin_profile', 'github_profile', 'twitter_profile', 'instagram_profile')

admin.site.register(CustomUser, CustomUserAdmin)

#super user : nami - nami2311 - nami@gmail.com

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_draft','category')

admin.site.register(Blog, BlogAdmin)