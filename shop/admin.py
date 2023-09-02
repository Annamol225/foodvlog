from django.contrib import admin
from .models import*

# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
admin.site.register(categ,catadmin)

class proadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug','stock','price','img','available']
    list_editable = ['stock','price','img','available']
admin.site.register(product,proadmin)
