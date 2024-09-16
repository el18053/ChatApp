from django import forms
class RoomCreationForm(forms.Form):
  name = forms.CharField(max_length=100, required=True)
class MessageForm(forms.Form):
  content = forms.CharField(widget=forms.Textarea)