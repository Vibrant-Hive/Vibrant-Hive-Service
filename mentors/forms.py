from django import forms
from django.forms import ModelForm

from mentors.models import User


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['active', 'availability', 'designation', 'email', 'experience', 'full_name', 'languages', 'password',
                  'rate', 'role', 'skills']
