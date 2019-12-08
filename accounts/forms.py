from django import forms
from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model



#User = get_user_model()
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ( 'last_name','email', 'username', 'password')
