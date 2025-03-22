from django import forms
from .models import Message

class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('title','text' , 'email')
        widgets = {
            "title" :forms.TextInput(attrs={
                "class" : "form-control",
                "placeholder" : "title"
            }),
            "text" :forms.Textarea(attrs={
                "class" : "form-control"
            })
        }