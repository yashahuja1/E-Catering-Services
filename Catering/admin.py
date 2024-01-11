from django.contrib import admin
# Register your models here.
from .models import*

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username']


class RAdmin(admin.ModelAdmin):
    list_display = ['id','Restaurant_Name']
    

admin.site.register(User,UserAdmin)
admin.site.register(Customer)
admin.site.register(Restaurant, RAdmin)
admin.site.register(Item)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(orderItem)
admin.site.register(Feedback)
admin.site.register(Contact)

