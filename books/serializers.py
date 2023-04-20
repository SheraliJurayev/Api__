from rest_framework import serializers
from .models import Book
from rest_framework.exceptions import ValidationError

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ('id' , 'title', 'subtitle' , 'content', 'author' ,  'isbn' , 'price',)

    def validate(self, data):
        title = data.get('title' , None)
        author = data.get('author' , None) 
        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False ,  
                    'message': "Kitob sarlavhasi harflardan tashkil topgan bo'lishi kerak "     
                }
            )
        if Book.objects.filter(title=title , author=author).exists :
             raise ValidationError(
                {
                    'status': False ,  
                    'message': "Bir xil sarlavhali va muallifli kitob yuklab bo'lmaydi"     
                }
            )

        
        return data  
    


    def validated_price(self , price):
        if price < 0 or price > 999999999 :
            raise ValidationError(
                {
                    'status': False ,  
                    'message': "Narx xato kiritildi."     
                }
            )
