from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={
            'placeholder': 'Email',
            'class': 'form-control',  })
        self.fields['password1'].widget = forms.TextInput(attrs={
            'placeholder': 'Password', 'class': 'form-control' ,'type':'password'})
        self.fields['password2'].widget = forms.TextInput(attrs={
            'placeholder': 'Confirm Password', 'class': 'form-control', 'type':'password'})
        self.fields['first_name'].widget = forms.TextInput(attrs={
            'placeholder': 'First Name', 'class': 'form-control'})
        self.fields['last_name'].widget = forms.TextInput(attrs={
            'placeholder': 'Last Name', 'class': 'form-control'})
        self.fields['username'].widget = forms.TextInput(attrs={
            'placeholder': 'Username', 'class': 'form-control'})