from django.http import HttpResponse
from django.shortcuts import render,  get_object_or_404
from . import models, forms

def book_view(request):
    book_value = models.Book.objects.all()
    return render(request, 'book.html', {'book_key': book_value})

def book_detail_view(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html', {'book_key': book_id})

def home(request):
    books = models.Book.objects.all()
    return render(request, 'book.html',{'book_key': books})

def createBookView(request):
    method = request.method
    if method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Коммент успешно добавлен</h1>')

    else:
        form = forms.ReviewForm()

    return render(request, 'create_review.html', {'form': forms})

def createLangPostView(request):
    method = request.method
    if method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно добавлен')
    else:
        form = forms.BookForm()
    return render(request, 'book.html', {'form': form})

def book_delete_view(request):
    lang_value = models.Book.objects.all()
    return render(request, 'del_book.html', {'lang_key': lang_value})

def book_drop_view(request, id):
    lang_id = get_object_or_404(models.Book, id=id)
    lang_id.delete()
    return HttpResponse('Успешно удален')