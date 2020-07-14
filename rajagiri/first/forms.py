from django.contrib.auth.models import User
from . models import Document
from django import forms

class UserForm(forms.ModelForm):
    CHOICES = [('select1', 'Admin'),
               ('select2', 'Doctor'),
               ('select3', 'Staff')]
    Type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password','first_name','last_name','Type']

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.Type = self.cleaned_data["Type"]
        if commit:
            user.save()
        return user


class AuthenticationForm(forms.ModelForm):
    password = forms.CharField(min_length=6, max_length=25, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','password']

class AddDocumentForm(forms.ModelForm):
    Document_image = forms.FileField()
    class Meta:
        model = Document
        fields = ['Hospital_id', 'Document_type', 'Document_image']
