from django import forms
from useraccounts.models import User
# # from django.contrib.auth.models import 


# class UserAccountForm(forms.ModelForm):
#     username = forms.CharField(max_length=256, widget=forms.TextInput(), help_text="UserName     ::")
#     email    = forms.CharField(max_length=256, widget=forms.EmailInput(), help_text="Email addr    ::")
#     password = forms.CharField(max_length=256, widget=forms.PasswordInput(), help_text="Password    ::")
    
#     # role     = forms.CharField(max_length=256, widget=forms.Select())

#     class Meta:
#         model  = User
#         fields = ('username', 'email', 'password')


class LoginForm(forms.ModelForm):
    # username = forms.CharField(max_length=256, widget=forms.TextInput(), help_text="UserName     ::")
    email    = forms.CharField(max_length=256, widget=forms.EmailInput(), help_text="Email addr    ::")
    password = forms.CharField(max_length=256, widget=forms.PasswordInput(), help_text="Password    ::")
    # role     = forms.CharField(max_length=256, widget=forms.Select())

    class Meta:
        model  = User
        fields = ( 'email', 'password')

# class TraderForm(forms.ModelForm):
#     occupation  = forms.CharField(required=False,max_length=256, widget=forms.TextInput(), help_text="UserName     ::")
#     phone       = forms.CharField(required=False,max_length=14, help_text="First name     ::")
#     fname       = forms.CharField(required=False,max_length=14, help_text="Last name     ::")
#     lname       = forms.CharField(required=False,max_length=14, help_text="Email addr    ::")
#     dob         = forms.CharField(required=False,max_length=14, help_text="Password    ::")

#     class Meta:
#         model = Trader
#         fields = ('occupation', 'fname', 'lname', 'dob', 'phone')

