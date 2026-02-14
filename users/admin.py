from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ("user", "created_on")
	search_fields = ("user__username", "user__email")
	list_select_related = ("user",)
	fields = ("user", "bio", "profile_image", "created_on")
	readonly_fields = ("created_on",)
