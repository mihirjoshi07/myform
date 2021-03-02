from django import forms

class myform(forms.Form):
    Name=forms.CharField()
    Email=forms.EmailField()
    Password=forms.CharField(widget=forms.PasswordInput)