from django import forms

from django.core.validators import URLValidator
from .validators import validate_dot_com, validate_url

class SubmitUrlForm(forms.Form):
    url = forms.CharField(
        label="", 
        validators=[validate_url, validate_dot_com],
        widget= forms.TextInput(
            attrs={
                "placeholder":"Long URL",
                "class":"form-control"
            }
        )
    )

    # def clean(self):
    #     cleaned_data = super(SubmitUrlForm, self).clean()
    #     #url = cleaned_data['url']
    #     #print(url)

    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     print(url)
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL for this field")
    #     return url