from django.shortcuts import render, redirect

from books.models import Book


def index(request):
    return redirect('books')


def books_view(request, pub_date=None):
    template = 'books/books_list.html'
    books = Book.objects.order_by('pub_date')
    context = {}
    if pub_date:
        pub_date = pub_date.date()
        context['prev_date'] = (
            books.filter(pub_date__lt=pub_date)
            .order_by('-pub_date')
            .values_list('pub_date', flat=True)
            .first()
        )
        context['next_date'] = (
            books.filter(pub_date__gt=pub_date)
            .values_list('pub_date', flat=True)
            .first()
        )
        books = books.filter(pub_date=pub_date)
    context['books'] = books
    return render(request, template, context)
