from django.shortcuts import render, get_object_or_404, redirect
from .models import Role
from .forms import RoleForm


# Create your views here.


def all_permissions(request):
    permissions = Role.objects.all()

    context = {
        'permissions': permissions,
    }

    return render(request, 'all_permissions.html', context)


def edit_permission(request, id):
    permission = get_object_or_404(Role, pk=id)

    if request.method == 'POST':
        form = RoleForm(request.POST, instance=permission)

        if form.is_valid():
            form.save()
            return redirect('/permissions/')
        else:
            print("NOT VALID")
            for e in form.errors:
                print(e)
            return redirect('/permissions/' + str(id) + '/edit_permission')
    else:
        form = RoleForm(instance=permission)
        return render(request, 'edit_article.html', {'form': form})


def delete_permission(request, id):
    permission = get_object_or_404(Role, pk=id)

    if permission:
        permission.delete()

    return redirect('/permissions/')
