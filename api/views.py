from django.shortcuts import render,redirect
from .models import Book1
from .forms import BookForm
from django.contrib import messages
from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)
                              
def Book_create(request):
    context={}
    if request.method == "POST": 
        form = BookForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Thank you! You have successfully  Added book")
                return redirect('/') 
            except:
                pass
        else:
            form=BookForm()           
            context['form']= form
    return render(request, "bookcreate.html", context)

def book_view(request):
    context ={}
    context["dataset"] = Book1.objects.all()
    return render(request, "booklist.html", context)  


# def booKEdit(request, id):
#     context ={}
#     context["data"] = Book1.objects.get(id = id)
#     return render(request, "bookedit.html", context)
 

# update view for Books
def bookUpdate(request, id):
    if request.method=='POST':
        obj = Book1.objects.get(id = id)
        form = BookForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
    else:
        obj = Book1.objects.get(id = id)
        form = BookForm(instance = obj)
    return render(request, "updatebook.html", {'form':form})      

def deleteBook(request, id):
    context ={}
    obj = get_object_or_404(Book1, id = id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
 
    # return render(request, "deletebook.html", context)
