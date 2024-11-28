from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


# login
# https://docs.djangoproject.com/en/5.1/topics/auth/default/#the-loginrequiredmixin-mixin
# from django.contrib.auth import logout, authenticate, login
# def my_view(request):
#     username = request.POST["username"]
#     password = request.POST["password"]
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.


# logout
# def logout_view(request):
#     logout(request)
#     # Redirect to a success page.