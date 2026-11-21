from django import forms


class SmsForm(forms.Form):
    phone_number = forms.CharField(
        label="Recipient phone number",
        help_text="Include the country code, for example +639171234567.",
        widget=forms.TextInput(attrs={"type": "tel", "autocomplete": "tel"}),
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={"rows": 5}),
    )
