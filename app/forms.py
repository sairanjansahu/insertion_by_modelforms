from django import forms
from app.models import *


class Topicform(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class Webpageform(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=['name']
        widgets={'url':forms.PasswordInput,'name':forms.Textarea}
        labels={'topic_name':'TN','name':'N'}
        help_texts={'topic_name':'should not be integers','name':'only Alphabets'}


class AccesRecordform(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'