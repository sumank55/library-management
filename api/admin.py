from django.contrib import admin
from .models import Book1,Category1,BookType1

# Register your models here.
class AdminBook(admin.ModelAdmin):
    list_display = ('category','btype','bookname','description','pub_date','price','cover_image')



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class BookTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)

admin.site.register(BookType1,BookTypeAdmin) 
admin.site.register(Book1,AdminBook)
 
admin.site.register(Category1,CategoryAdmin) 
 

