from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published_year', 'quantity')
    search_fields = ('title', 'author', 'category')
    list_filter = ('category', 'published_year')

admin.site.register(Book, BookAdmin)

