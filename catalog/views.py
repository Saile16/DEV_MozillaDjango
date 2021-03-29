from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
# Create your views here.
# Todo lo que hicimos con clase verificar despues si podemos usarlo todo en funciones
# como en la app blog de ClevP
####


def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Libros disponibles (status = 'a' =>Aviable)
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()
    # El 'all()' esta implícito por defecto.
    num_authors = Author.objects.count()
    num_genre = Genre.objects.count()
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre': num_genre
    }
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(request, 'index.html', context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    # your own name for the list as a template variable
    # context_object_name = 'my_book_list'
    # queryset = Book.objects.filter(title__icontains='war')[
    #     :5]  # Get 5 books containing the title war
    # # Specify your own template name/location
    # template_name = 'books/book_detail.html'

    def get_queryset(self):
        # Get 5 books containing the title war
        return Book.objects.filter(title__icontains='e')[:5]

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Get the blog from id and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Author
