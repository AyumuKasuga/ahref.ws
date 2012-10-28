from django import forms


class AddUrlForm(forms.Form):
    url = forms.URLField(label='Url', required=True)