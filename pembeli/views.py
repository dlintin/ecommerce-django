from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akun dibuat untuk {username}!, Silahkan Login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form':form})




@login_required
def akun(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,  instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profil telah diupdate!')
            return redirect('akun-home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render (request, 'account-details.html',context)

# jika menggunakan gambar
# @login_required
# def akun(request):
#     if method == 'POST': 
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         # jika menggunakan gambar
#         p_form = ProfilUpdateForm(request.POST, request.FILES, instance=request.user.profil)
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfilUpdateForm(instance=request.user.profil)
#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }
#     return render (request, 'account-details.html',context)