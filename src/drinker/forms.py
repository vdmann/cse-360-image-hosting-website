from django import forms
from django.contrib.auth.models import User

# provide the ability to pass a model out of the form to create fields
from django.forms import ModelForm
from drinker.models import Drinker


class RegistrationForm(ModelForm):
    # u' <-- is the unicode string
    username    = forms.CharField(label=(u'User Name'))
    email       = forms.EmailField(label=(u'Email Address'))
    # using Django's default widget, which will make a password field which hides it as you type 
    password    = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password1   = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))

    class Meta:
        # takes all the attributes of the RegistrationForm and creates a model
        model = Drinker
        # since we already created user field parameters.
        exclude = ('user','file')
        
    def clean_username(self):
        # data comming back from the form after posting it to the view, get what ever is from user to store it in username locally
        username = self.cleaned_data['username']
        try:
                # try and get any user object that is submitted in the form
                User.objects.get(username=username)
        # if the username does not exists you can use this username
        except User.DoesNotExist:
                return username
        raise forms.ValidationError("That username is already taken, please select another.")

    # clean method gets access to all the attributes submitted into the form
    def clean(self):
        # check if the passwords match then throw a validation error
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError("The passwords did not math. Pleate try again.")
        return self.cleaned_data


class LoginForm(forms.Form):
    username    = forms.CharField(label=(u'User Name'))
    password    = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))