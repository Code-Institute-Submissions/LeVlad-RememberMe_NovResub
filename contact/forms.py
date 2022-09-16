from django import forms


class ContactForm(forms.Form):
    """
    A form class for contact
    """
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
