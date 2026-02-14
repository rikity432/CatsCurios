from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.generic import CreateView, DetailView, UpdateView

from blog.models import Comment

from .forms import ProfileForm


class SignUpView(CreateView):
	form_class = UserCreationForm
	template_name = "registration/signup.html"

	def form_valid(self, form):
		self.object = form.save()
		login(self.request, self.object)
		messages.success(self.request, "Account created. You're now logged in.")

		next_url = self.request.POST.get("next") or self.request.GET.get("next")
		if next_url and url_has_allowed_host_and_scheme(
			next_url,
			allowed_hosts={self.request.get_host()},
			require_https=self.request.is_secure(),
		):
			return redirect(next_url)

		return redirect(reverse("home"))


class ProfileDetailView(DetailView):
	model = User
	template_name = "users/profile.html"
	context_object_name = "profile_user"

	def get_object(self, queryset=None):
		return get_object_or_404(User, username=self.kwargs.get("username"))

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		profile_user = self.object

		context["profile"] = getattr(profile_user, "profile", None)
		context["recent_comments"] = (
			Comment.objects.filter(user=profile_user)
			.select_related("post")
			.order_by("-created_on")[:10]
		)
		return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
	form_class = ProfileForm
	template_name = "users/profile_edit.html"

	def get_object(self, queryset=None):
		return self.request.user.profile

	def form_valid(self, form):
		messages.success(self.request, "Profile updated.")
		return super().form_valid(form)

	def get_success_url(self):
		return reverse("profile", kwargs={"username": self.request.user.username})
