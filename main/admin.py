from django.contrib import admin
from main.models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['adress', 'number', 'message']
    search_fields = ['adress', 'number', 'message']
    list_editable = ['number']
admin.site.register(Contact, ContactAdmin)