from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models, forms

class BookView(generic.ListView):
    template_name = 'book.html'
    queryset = models.Book.objects.all()

    def get_queryset(self):
        return models.Book.objects.all()

class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'

    def get_object(self, **kwargs):
        lang = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=lang)

class CreateBookPostView(generic.CreateView):
    template_name = 'book.html'
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBookPostView, self).form_valid(form=form)

class UpdateBookPostView(generic.UpdateView):
    template_name = 'update_book.html'
    form_class = forms.BookForm
    success_url = '/'

    def get_object(self, **kwargs):
        lang = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=lang)

    def form_valid(self, form):
        return super(UpdateBookPostView, self).form_valid(form=form)

class BookDropView(generic.DeleteView):
    template_name = 'confirm_del.html'
    success_url = '/'

    def get_object(self, **kwargs):
        lang_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=lang_id)

class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'object_list'  # изменено с 'book'
    paginate_by = 5

    def get_queryset(self):
        return models.Book.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

def createBookView(request):
    if request.method == 'POST':
        form = forms.BookForm(request.POST)
        if form.is_valid():
            # Обработка формы
            pass
    else:
        form = forms.BookForm()
    return render(request, 'create_review.html', {'form': form})
