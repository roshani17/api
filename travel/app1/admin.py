from django.contrib import admin
from .models import destination
from .models import destinationName


class destinationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'disc',
        'price'
    )


# Register your models here.

admin.site.register(destination, destinationAdmin)

admin.site.register(destinationName)
