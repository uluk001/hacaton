from django.contrib import admin
from main.models import Contact


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ("id","name", "email", "addres", "message", "sent_at")

admin.site.register(Contact,  ContactAdmin)