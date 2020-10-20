from django import forms

class RegisterForm(forms.Form):
    team_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.NumberInput()
    check = forms.CheckboxInput()
    upload = forms.FileField()
