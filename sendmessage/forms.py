# from django import forms

# class MessageForm(forms.Form):
#     phone_number = forms.CharField(max_length=100, required=True)
#     message = forms.CharField(widget=forms.Textarea, required=True)


from django import forms

class MessageForm(forms.Form):
    phone_number = forms.CharField(
        max_length=100,
        required=True,
        label="Phone Numbers (separated by commas)",
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. 9876543210, 9876543211, 9876543212'
        })
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': 'Type your message here...',
            'rows': 5
        })
    )
