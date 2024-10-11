from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('pk','title','author')
    search_fields =('title','pk')
# Register your models here.
admin.site.register(Book,BookAdmin)
