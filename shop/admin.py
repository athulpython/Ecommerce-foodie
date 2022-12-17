from django.contrib import admin
from . models import *
# Register your models here.
class catagdmin(admin.ModelAdmin):

    prepopulated_fields={'slug':('name',)}
    list_display = ['name', 'slug']
admin.site.register(categ,catagdmin)


class prodadmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','img','available','desc']
    list_editable=['price','stock','img','available','desc']
    prepopulated_fields={'slug':('name',)}
admin.site.register(products,prodadmin)