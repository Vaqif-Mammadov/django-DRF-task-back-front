from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Books
from .forms import BooksForm


def books_view(request):
    books=Books.objects.all()
    return render(request, 'books.html', {'books': books})

def api_view(request):
    return render(request,'withapi.html')

def add_book_view(request):
    form=BooksForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        book=form.save(commit=False)
        book.save()
        messages.success(request, 'Kitabiniz bazaya elave olundu')
        return redirect('books')
    return render(request,'addbook.html',{'form':form})