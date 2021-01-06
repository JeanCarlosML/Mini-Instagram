from django.contrib import admin

# Register your models here.
from users.models import Profile
#Registrarlo en el dashboard de admin  
#admin.site.register(Profile)
@admin.register(Profile) 
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','phone_number')
    pass