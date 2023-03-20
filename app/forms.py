from django import forms
from app.models import *

class Userfrom(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        widgets={'password':forms.PasswordInput}
class Profileform(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','Profile_pic']
        widgets={'address':forms.Textarea(attrs={'cols':20,'rows':10})}
