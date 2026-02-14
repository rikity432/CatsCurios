from django.urls import path

from .views import ProfileDetailView, ProfileEditView

urlpatterns = [
    path("profile/edit/", ProfileEditView.as_view(), name="profile_edit"),
    path("profile/<str:username>/", ProfileDetailView.as_view(), name="profile"),
]
