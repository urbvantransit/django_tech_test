from django import forms
from .models import Users
# Create your forms here

class UsersModelForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = [
            'first_name',
            'last_name',
            'email_user',
            'phone_user',
            'pass_user',
        ]
