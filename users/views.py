from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.generic import CreateView


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
