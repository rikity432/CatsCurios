from django import forms
from django.core.exceptions import ValidationError

from .models import Profile


class ProfileForm(forms.ModelForm):
    MAX_BIO_CHARS = 500
    MAX_IMAGE_BYTES = 2 * 1024 * 1024  # 2MB

    class Meta:
        model = Profile
        fields = ("location", "bio", "profile_image")
        widgets = {
            "location": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Dublin, Ireland",
                    "maxlength": "100",
                }
            ),
            "bio": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Tell us about yourself...",
                    "maxlength": "500",
                }
            ),
            "profile_image": forms.ClearableFileInput(
                attrs={
                    "accept": "image/*",
                }
            ),
        }

        help_texts = {
            "location": "Optional. Max 100 characters.",
            "bio": "Max 500 characters.",
            "profile_image": "Optional. JPG/PNG/WEBP recommended (max 2MB).",
        }

    def clean_location(self):
        location = (self.cleaned_data.get("location") or "").strip()
        if len(location) > 100:
            raise ValidationError("Location must be 100 characters or less.")
        return location

    def clean_bio(self):
        bio = (self.cleaned_data.get("bio") or "").strip()
        if len(bio) > self.MAX_BIO_CHARS:
            raise ValidationError(
                f"Bio must be {self.MAX_BIO_CHARS} characters or less."
            )
        return bio

    def clean_profile_image(self):
        upload = self.cleaned_data.get("profile_image")
        if not upload:
            return upload

        content_type = getattr(upload, "content_type", "") or ""
        if content_type and not content_type.startswith("image/"):
            raise ValidationError("Please upload an image file.")

        size = getattr(upload, "size", None)
        if size is not None and size > self.MAX_IMAGE_BYTES:
            raise ValidationError("Image must be 2MB or smaller.")

        return upload
