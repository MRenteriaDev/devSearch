from django.db.models.base import Model
from django.forms import ModelForm, fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Messages, Profile, Skills

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email','username','password1','password2']
        labels = {
            'first_name': "Name",
            "email": "Email"
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})



class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','username','location','bio','short_intro','profile_image',
        'social_github','social_linkedin','social_youtube','social_twitter','social_website']

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class InboxForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['name','email','subject','body']

    def __init__(self, *args, **kwargs):
        super(InboxForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
