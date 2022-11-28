from django import forms
  
# creating a django form
class GeeksForm(forms.Form):
	title = forms.CharField(widget = forms.Textarea)
	description = forms.CharField(widget = forms.CheckboxInput)
	views = forms.IntegerField(widget = forms.TextInput)
	available = forms.BooleanField(widget = forms.Textarea)
