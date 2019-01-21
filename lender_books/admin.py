"""To register model Book with admin."""
from django.contrib import admin
from .models import Book


admin.site.register((Book,))
