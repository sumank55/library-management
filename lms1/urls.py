
from django.contrib import admin
from django.urls import path
from api import views
from django.conf.urls.static import static
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/',views.Book_create,name='book'),
    path('',views.book_view,name='booklist'),
    path('<int:id>/',views.bookUpdate,name='update'),
    path('delete/<id>/',views.deleteBook,name='delete')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

