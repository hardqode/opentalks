from django import forms
from allauth.account.forms import SignupForm as SForm
from django.forms import ModelForm

class SignupForm(SForm):
    instagram = forms.URLField(max_length=100, label='Instagram', required=False)
    facebook = forms.CharField(max_length=100, label='Facebook',required=False)
    about = forms.CharField(max_length=1000, label='About me', required=False)

    def save(self, request):
        user = super(SignupForm, self).save(request)
        user.instagram = self.cleaned_data['instagram']
        user.facebook = self.cleaned_data['facebook']
        user.save()
        return user