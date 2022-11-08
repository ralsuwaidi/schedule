from django.contrib import admin

from .models import EventModel, PermitModel


class EventAdmin(admin.ModelAdmin):
    pass

class PermitAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(EventModel, EventAdmin)
admin.site.register(PermitModel, PermitAdmin)