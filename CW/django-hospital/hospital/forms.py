from django import forms
from .models import *


class DForm(forms.ModelForm):
    model = User
    fileds = ['national_code', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields["national_code"].widget.attrs.update({
            "class": "form-control text-success",
            "placeholder": "National code",
        })
        
        self.fields["password1"].widget.attrs.update({
            "class": "form-control text-success",
            "type": "password",
            "placeholder": "set Password",
        })
                
        self.fields["password2"].widget.attrs.update({
            "class": "form-control text-success",
            "type": "password",
            "placeholder": "check Password",
        })
        
        