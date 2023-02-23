# @Project:     HardwareHive
# @Filename:    forms.py
# @Author:      Daksh
# @Time:        23-02-2023 02:14 pm
from django import forms

from .models import ChatMessage

FORM_CSS = 'w-full py-4 px-6 rounded-xl border'


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': FORM_CSS
            })
        }
