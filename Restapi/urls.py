
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Books.views import books_view, add_book_view, api_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books-api/', include('Books.api.urls')),
    path('books/', books_view,name='books'),
    path('addbook/', add_book_view,name='addbook'),
    path('withapi/', api_view,name='withapi'),


]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)