from django import forms

class MessageForm(forms.Form):
    phone_number = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
