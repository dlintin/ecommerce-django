from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.
def registrasi(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akun dibuat untuk {username}!')
            return redirect('barang-home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form':form})