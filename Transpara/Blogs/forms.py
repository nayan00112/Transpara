from django import forms

class FeedBackForm(forms.Form):
    topic_title = forms.CharField(max_length=50, required=True)
    feedbackmessage = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':34}), required=True)