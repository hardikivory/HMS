
from .models import Guest, User, Worker,Room,Contact

from django import forms



class UserRegisterForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password'].widget.attrs.update({'class' : 'form-control'})

class UserLoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'password']


    def clean(self):
        val_username = self.cleaned_data.get('username')
        val_password = self.cleaned_data.get('password')
        
        user = User.objects.filter(username = val_username, password = val_password)
       
        
        if user:
            print('success...')
            
        else:
            raise forms.ValidationError('Invalid Credentials....')
            


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password'].widget.attrs.update({'class' : 'form-control'})




class GuestUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Guest
        fields = ['username', 'first_name', 'last_name', 'father_name', 'age', 'gender', 'email', 'phn_no', 'native_address', 'work_address']

       
     

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['father_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['age'].widget.attrs.update({'class' : 'form-control'})
        self.fields['gender'].widget.attrs.update({'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        self.fields['phn_no'].widget.attrs.update({'class' : 'form-control'})
        self.fields['native_address'].widget.attrs.update({'class' : 'form-control'})
        self.fields['work_address'].widget.attrs.update({'class' : 'form-control'})
        # self.fields['password'].widget.attrs.update({'class' : 'form-control'})


class WorkerUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Worker
        fields = ['username', 'first_name', 'last_name', 'age', 'gender', 'email', 'phn_no', 'native_address', 'current_address']

        

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['age'].widget.attrs.update({'class' : 'form-control'})
        self.fields['gender'].widget.attrs.update({'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        self.fields['phn_no'].widget.attrs.update({'class' : 'form-control'})
        self.fields['native_address'].widget.attrs.update({'class' : 'form-control'})
        self.fields['current_address'].widget.attrs.update({'class' : 'form-control'})
        # self.fields['password'].widget.attrs.update({'class' : 'form-control'})



class RoomForm(forms.ModelForm):    
    class Meta:
        model = Room
        fields = ['room_type']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['room_type'].widget.attrs.update({'class' : 'form-control'})
       


class ContactForm(forms.ModelForm):
    
    
    class Meta:
        model = Contact
        fields = "__all__"
        

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        self.fields['phn_no'].widget.attrs.update({'class' : 'form-control'})
        self.fields['desc'].widget.attrs.update({'class' : 'form-control'})