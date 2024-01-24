from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """Model for the profile display form on the profile page"""

    class Meta:
        model = UserProfile
        exclude = ('user',)


    def __init__(self, *args, **kwargs):
        """
        Add placeholders and set autofocus on the first field in the form. 
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields['default_phone_number'].widget.attrs['autofocus']=True
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
