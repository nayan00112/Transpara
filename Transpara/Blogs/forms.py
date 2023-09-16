from django import forms

class FeedBackForm(forms.Form):
    email = forms.EmailField(required=True)
    feedbackmessage = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':34}), required=True)