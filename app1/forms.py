from django import forms
from .models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"

    def clean_mobile(self):
        data = self.cleaned_data['mobile']
        if len(data) != 10 or not data.isdigit():
            raise forms.ValidationError("Mobile number must be a 10-digit number.")
        return data