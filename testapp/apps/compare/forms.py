from django import forms

class InputForm(forms.Form):
    string = forms.CharField(label='string', required=True)

    def get_string(self):

        return self.cleaned_data.get('string') or None