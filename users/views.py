from django.conf import settings
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm

REDIDECT_URL = settings.LOGIN_REDIRECT_URL


class CustomLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(REDIDECT_URL)
        """Handle GET requests: instantiate a blank version of the form."""
        return self.render_to_response(self.get_context_data())


# def CustomLoginView(request):
#     print("Custom LoginView Called")
#     return HttpResponse("hello")


def register_user(request):

    if request.user.is_authenticated:
        return redirect(REDIDECT_URL)

    else:
        form = CustomUserCreationForm()
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()

                return redirect(settings.LOGIN_URL)

    context = {"form": form}

    return render(request, "register.html", context)
