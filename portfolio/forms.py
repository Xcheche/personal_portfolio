# myapp/forms.py
from django import forms
from .models import Contact
import re


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "message"]

        # labels
        labels = {
            "name": "Your Name",
            "email": "Your Email",
            "phone": "Your Phone Number",
            "message": "Your Message",
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter your FullName"}),
            "email": forms.EmailInput(
                attrs={"placeholder": "Enter a valid email must have @ character "}
            ),
            "phone": forms.TextInput(
                attrs={"placeholder": "Enter your phone number eg. +2347048706554"}
            ),
            "message": forms.Textarea(attrs={"placeholder": "Enter your message"}),
        }

    # Validating forms.py  there are amny ways to validate a form in django
    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not re.match(r"^\+?1?\d{9,15}$", phone):
            raise forms.ValidationError(
                "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        return phone

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "@" not in email:
            raise forms.ValidationError("Email must be valid.")
        return email
