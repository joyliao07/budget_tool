"""To render html views with its content."""
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import login_required


@login_required
def book_detail_view(request, pk=None):
    """To render book_detail_view with its content."""
    context = {
        'book': get_object_or_404(Book, id=pk)
    }

    return render(request, 'books/book_detail.html', context)


@login_required
def book_list_view(request):
    """To render book_list_view with its content."""
    context = {
        'books': get_list_or_404(Book)
    }

    return render(request, 'books/book_list.html', context)
