from django.urls import path
from . import views

urlpatterns = [
    path(
        route="signup/",
        view=views.SignUpView.as_view(),
        name="signup"
    ),
    path(
        route="signin/",
        view=views.SignInView.as_view(),
        name="signin"
    ),
    path(
        route="verify_email/",
        view=views.VerifyEmailView.as_view(),
        name="verify_email"
    ),
    path(
        route="change_password/",
        view=views.ChangePasswordView.as_view(),
        name="change_password"
    ),
    path(
        route="delete_account/",
        view=views.DeleteAccountView.as_view(),
        name="delete_account"
    )
]
