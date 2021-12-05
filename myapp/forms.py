from django import forms
from .models import UserDetail
class UserForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        # name = forms.CharField()
        # image = forms.FileField()
        # age = forms.IntegerField()
        # email = forms.EmailField()
        # place = forms.CharField()
        # occupation = forms.CharField()
        fields = ('name', 'image', 'age', 'email', 'place', 'occupation','gender')

        widgets={
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'image' : forms.FileInput(attrs={'class':'form-control','placeholder':'Image Url'}),
            'age' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Age'}),
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'place' : forms.TextInput(attrs={'class':'form-control','placeholder':'Place'}),
            'occupation' : forms.TextInput(attrs={'class':'form-control','placeholder':'Occupation'}),
            'gender' : forms.TextInput(attrs={'class':'form-control','placeholder':'Gender'}),

        }
    

    
    