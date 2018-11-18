from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .models import Account
from django.contrib.auth.models import User
from .forms import UserForm, AccountForm


# Create your views here.


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def all_users(request):
    users = User.objects.all()

    for user in users:
        print(user.username)
        for role in user.account.roles.all():
            print('-- ' + str(role))

    context = {
        'users': users,
    }

    return render(request, 'users.html', context)


def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    account = user.account
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        account_form = AccountForm(request.POST, request.FILES, instance=account)

        if user_form.is_valid() and account_form.is_valid():
            user_form.save()
            account_form.save()
            return redirect('accounts:all_users')
        else:
            print("noooooooooooot valid")
            print("user form", user_form.errors)
            print("account form", account_form.errors)
            return redirect('accounts:edit_user', user_id)
    else:
        user_form = UserForm(instance=user)
        account_form = AccountForm(instance=account)
        return render(request, 'edit_user.html', {'user_form': user_form, 'account_form': account_form})
