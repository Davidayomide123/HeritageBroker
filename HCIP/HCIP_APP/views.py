from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import *

# Import the custom decorator
from .decorators import unauthenticated_user

def home(request):
    return render(request, 'HCIP_APP/index.html')

@unauthenticated_user  
def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')  # Adjust as per your form field
            messages.success(request, f'Your account has been created successfully! {user}')
            return redirect('LoginPage')  # Replace with your success URL
    else:
        form = MyUserCreationForm()

    context = {'form': form}
    return render(request,'HCIP_APP/register.html', context)

@unauthenticated_user
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back {username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password is incorrect.')

    return render(request, 'HCIP_APP/login.html')

@login_required(login_url='LoginPage')
def dashboard(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where UserProfile does not exist
        user_profile = None  # Or any default behavior you want

    context = {
        'user_profile': user_profile,
        # other context variables as needed
    }
    context = {'user_profile':user_profile}
    return render(request, 'HCIP_APP/dashboard.html', context)

@login_required(login_url='LoginPage')
def LogoutPage(request):
    logout(request)
    return redirect('LoginPage')

@login_required(login_url='LoginPage')
def Bank_Deposit(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {'user_profile':user_profile}
    return render(request, 'HCIP_APP/bank_deposit.html', context)

@login_required(login_url='LoginPage')
def Success(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {'user_profile':user_profile}
    return render(request, 'HCIP_APP/success.html', context)

@login_required(login_url='LoginPage')
def basic(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user
    
    if request.method == 'POST':
        form = InvestmentForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Your investment has been successfully placed.')
                return redirect('dashboard')  # Replace 'dashboard' with your actual dashboard URL name
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = InvestmentForm(user_profile=user_profile)
    
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'HCIP_APP/basic.html' , context)

@login_required(login_url='LoginPage')
def copy_trade(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {'user_profile':user_profile}
    return render(request, 'HCIP_APP/copy_trade.html' , context)

@login_required(login_url='LoginPage')
def crypto_deposit(request):
    user_profile = request.user.userprofile  # Assuming UserProfile is related to user through OneToOneField

    if request.method == 'POST':
        form = DepositForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('deposit_review_page')  # Redirect to deposit review page upon successful deposit
    else:
        form = DepositForm(instance=request.user.userprofile)
    context = {'user_profile':user_profile,
               'form':form,
               }
    return render(request, 'HCIP_APP/crypto_deposit.html', context)

@login_required(login_url='LoginPage')
def deposit_review_page(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {'user_profile':user_profile}
    return render(request, 'HCIP_APP/review.html', context)

@login_required(login_url='LoginPage')
def deposit(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {'user_profile':user_profile}
    return render(request, 'HCIP_APP/deposit.html', context)

@login_required(login_url='LoginPage')
def investment(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {'user_profile':user_profile}
    return render(request, 'HCIP_APP/investment.html', context)

@login_required(login_url='LoginPage')
def kyc(request):
    return render(request, 'HCIP_APP/kyc.html')

@login_required(login_url='LoginPage')
def nok(request):
    return render(request, 'HCIP_APP/nok.html')

@login_required(login_url='LoginPage')
def notification(request):
    return render(request, 'HCIP_APP/notification.html')

@login_required(login_url='LoginPage')
def premium(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user
    
    if request.method == 'POST':
        form = InvestmentForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Your investment has been successfully placed.')
                return redirect('dashboard')  # Replace 'dashboard' with your actual dashboard URL name
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = InvestmentForm(user_profile=user_profile)
    
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'HCIP_APP/premium.html' , context)

@login_required(login_url='LoginPage')
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {'user_profile':user_profile}
    return render(request, 'HCIP_APP/profile.html', context)

@login_required(login_url='LoginPage')
def refferal(request):
    return render(request, 'HCIP_APP/refferal.html')

@login_required(login_url='LoginPage')
def signals(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {'user_profile':user_profile}
    return render(request, 'HCIP_APP/signals.html' , context)

@login_required(login_url='LoginPage')
def standard(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user
    
    if request.method == 'POST':
        form = InvestmentForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Your investment has been successfully placed.')
                return redirect('dashboard')  # Replace 'dashboard' with your actual dashboard URL name
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = InvestmentForm(user_profile=user_profile)
    
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'HCIP_APP/standard.html' , context)

@login_required(login_url='LoginPage')
def terms(request):
    return render(request, 'HCIP_APP/terms.html')

@login_required(login_url='LoginPage')
def ultimate(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user
    
    if request.method == 'POST':
        form = InvestmentForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Your investment has been successfully placed.')
                return redirect('dashboard')  # Replace 'dashboard' with your actual dashboard URL name
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = InvestmentForm(user_profile=user_profile)
    
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'HCIP_APP/ultimate.html', context)

@login_required(login_url='LoginPage')
def withdrawal(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {'user_profile':user_profile}
    return render(request, 'HCIP_APP/withdrawal.html', context)