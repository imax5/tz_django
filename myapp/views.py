from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import RegisterForm
from .tasks import task_register_email


def index(request):
    return render(request, 'index.html')

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # task_register_email.delay(user.pk)
            messages.success(request, f'{user.username}. You have registered successfully!')
            return redirect('index')
        else:
            messages.error(request, 'form is invalid')
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)