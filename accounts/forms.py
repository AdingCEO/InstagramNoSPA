from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name']
        
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.save()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'last_name', 'website_url', 'bio', 'phone_number', 'gender']