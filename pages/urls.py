from django.urls import path

from .views import HomePageView, ProjectsView, DeveloperView, ContactView, ImprintView, PrivacyView, SuccessView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("projects/", ProjectsView.as_view(), name="projects"),
    path("developer/", DeveloperView.as_view(), name="developer"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("imprint/", ImprintView.as_view(), name="imprint"),
    path("privacy/", PrivacyView.as_view(), name="privacy"),
    path("contact/success/", SuccessView.as_view(), name="success_page")
]