from django.contrib import admin
from .models import TicketOrder, Member

# Register your models here.

admin.site.register(TicketOrder)
admin.site.register(Member)