from django.conf.urls import url

from . import views


urlpatterns = [
    # esto de los URL creo que podemos hacerlos con paths si usamos las views como funciones
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$',
        views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^borrowed/$', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
    url(r'^book/(?P<pk>[-\w]+)/renew/$',
        views.renew_book_librarian, name='renew-book-librarian'),
    # Actalizar, Crear, Eliminar autores
    url(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    url(r'^author/(?P<pk>\d+)/update/$',
        views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^author/(?P<pk>\d+)/delete/$',
        views.AuthorDelete.as_view(), name='author_delete'),
    # Actalizar, Crear, Eliminar libros
    url(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    url(r'^book/(?P<pk>\d+)/update/$',
        views.BookUpdate.as_view(), name='book_update'),
    url(r'^book/(?P<pk>\d+)/delete/$',
        views.BookDelete.as_view(), name='book_delete'),
]
