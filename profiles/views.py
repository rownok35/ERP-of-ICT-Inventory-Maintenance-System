from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.forms import SignUpForm, ProfileForm
from profiles.models import NewUser



# Create your views here.

def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!")
            return HttpResponseRedirect(reverse('profiles:index'))
    return render(request, 'profiles/sign_up.html', context={'form':form})




@login_required
def index(request):
    return HttpResponseRedirect(reverse('product:items'))


def login_page(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('product:items'))

    return render(request, 'profiles/login.html', {})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('profiles:login'))

@login_required
def profile(request):
    return render(request, 'profiles/profile.html', context={})


@login_required
def user_profile(request):
    profile = NewUser.objects.get(user_name=request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance= profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Change Saved!!")
            form = ProfileForm(instance=profile)
            return HttpResponseRedirect(reverse('profiles:profile'))
    return render(request, 'profiles/change_profile.html', context={'form':form})


@login_required
def pass_change(request):
    current_user = request.user

    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password Changed Successfully!")
            return HttpResponseRedirect(reverse('profiles:profile'))
    return render(request, 'profiles/change_pass.html', context={'form': form})