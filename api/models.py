from django.db import models

# Create your models here.

class Category1(models.Model):
    name=models.CharField(max_length=100)


    def __str__(self):
        return str(self.name)

class BookType1(models.Model):
    type=models.CharField(max_length=100)

    def __str__(self):
        return str(self.type)        


class Book1(models.Model):
    # bookid=models.CharField(max_length=10)
    btype = models.ForeignKey(BookType1,on_delete=models.CASCADE)
    category = models.ForeignKey(Category1,on_delete=models.CASCADE)
    bookname=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    pub_date=models.DateField()
    price=models.FloatField()
    cover_image = models.ImageField(null= True, blank=True,upload_to='uploads/images/')
#     TYPE = (
    #        ('Sports','Sports'),
#        ('Educational', 'Educational'),
#        ('Motivationa','Motivational')
#    )
#     type = models.CharField(
#        max_length=30,
#        choices=TYPE,
#        default='available',
#    )

    def __str__(self):
        return str(self.bookname)
