from django import forms
from .models import Book1,Category1,BookType1
 
 
class BookForm(forms.ModelForm):
    class Meta:
        model = Book1
        fields = ['bookname','category','btype','description','pub_date','price','cover_image']
        # widgets={
        #     'bookname': forms.TextInput(attrs={'class':'form-control'}),
        #     # 'category': forms.TextInput(attrs={'class':'form-control'}),
        #     # 'btype': forms.TextInput(attrs={'class':'form-control'}),
        #     'description': forms.TextInput(attrs={'class':'form-control'}),
        #     'pub_date': forms.DateField(attrs={'class':'form-control'}),
        #      'price': forms.FloatField(attrs={'class':'form-control'}),
        #     'cover_image': forms.ImageField(attrs={'class':'form-control'}),

        # }

