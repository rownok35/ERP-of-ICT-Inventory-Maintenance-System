from django.forms import ModelForm
from profiles.models import NewUser

from django.contrib.auth.forms import UserCreationForm




class SignUpForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ('user_name', 'email', 'password1', 'password2',)


class ProfileForm(ModelForm):
    class Meta:
        model = NewUser
        fields = ('email', 'picture', 'user_name', 'department', 'rank', 'mobile_1', 'mobile_2', 'password' )
    
    def clean(self):
        pass
        

