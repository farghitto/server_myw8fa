from django.contrib import admin
from .models import EmailAzienda

# Register your models here.


class EmailAziendaModelAdmin(admin.ModelAdmin):
    model = EmailAzienda
    
    list_display = [field.name for field in EmailAzienda._meta.get_fields()]
    search_fields = [field.name for field in EmailAzienda._meta.get_fields()]




admin.site.register(EmailAzienda, EmailAziendaModelAdmin)

# Register your models here.
