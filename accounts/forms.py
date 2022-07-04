from jsonschema import ValidationError
from .models import User

from django import forms
class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'age', 'gender','email', 'password']

        
    
    def clean(self):
        cleaned_data  = super().clean()
        val_username = self.cleaned_data.get('username')
        
        check_username = User.objects.filter(username = val_username)
       
        if check_username:
            
            raise forms.ValidationError('Username Already Exist.')
        
        
        return val_username
    
 
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['age'].widget.attrs.update({'class' : 'form-control'})
        self.fields['gender'].widget.attrs.update({'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password'].widget.attrs.update({'class' : 'form-control'})
       

    