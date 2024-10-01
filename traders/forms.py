from django import forms
from django.core.exceptions import ValidationError

from .models import Product

class ProductForm(forms.ModelForm):
    '''
    The NotesForm class "is a" Model Form (the inheritance)
    It says that anything that is a NotesForm will have the characteristics
    defined by the "Meta" elements. 
    Also, All NotesForms and its "fields" will conform to the 
    Dependency Injections (validations) specified in the 
    "clean_"fieldname methods.  
    While this may seem overkill for creating a form,
    keep in mind that this will be (re-)used for both Create and Update.  
    '''
    class Meta:
        '''
        A "Meta Class defines information about the class itself.
        Notice here that we are defining what the NotesForm (Not a note)
        will have or know about.        
        '''
        model = Product
        fields = ('name', 'description', 'price', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control my-2"}),
            'description': forms.Textarea(attrs={'class': "form-control mt-2"}),
            'price': forms.NumberInput(attrs={'class': "form-control mt-2"}),
            'image': forms.ClearableFileInput(attrs={'class': "form-control mt-2"}),  # Add widget for the image
        }
        labels = {
			'name': 'Product Name',
   			'description': 'Product Description',
            'price': 'Product Price',
            'image': 'Product Image'
		}
        
    def clean_price(self):
        '''
        This method validates the price field.
        '''
        price = self.cleaned_data['price']
        
        # Ensure price is a positive number
        if price <= 0:
            raise ValidationError("Price must be a positive number")
        
        return price