from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages

from task_manager.user.forms import UserForm
from task_manager.user.models import User

class IndexView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, "users/index.html", {"users": users})


class UserFormCreateView(View):
    def get(self, request):
        form = UserForm()
        return render(
            request,
            'users/create.html',
            {'form': form},
        )

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Статья создана.")
            return redirect("user_index")

        messages.add_message(request, messages.WARNING, "Не удалось создать статью.")
        return render(
            request,
            "users/create.html",
            {"form": form},
        )