from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Ustadz)
admin.site.register(Mahasantri)
#admin.site.register(Setoran)
admin.site.register(Kitab)

@admin.register(Setoran)
class Setoran(admin.ModelAdmin):
    list_display = ['id', 'mahasantri', 'kitab', 'date_created','nilai','ketengan'  ]
    list_filter = ['mahasantri']
    

