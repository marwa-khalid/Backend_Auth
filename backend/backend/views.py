from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import BrandManagerRegistrationForm
from .forms import PRManagerRegistrationForm
from django.contrib import messages
from .forms import PRLoginform
from .forms import AdminLoginform

def brandmanager_register(request):
    if request.method == 'POST':
        form = BrandManagerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = BrandManagerRegistrationForm()
    return render(request, 'templates/brandmanager_register.html', {'form': form})

def brandmanager_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_active and user.is_brand_manager:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'templates/brandmanager_login.html', {'error_message': 'Your account is not a brand manager account.'})
        else:
            return render(request, 'templates/brandmanager_login.html', {'error_message': 'Invalid login credentials.'})
    else:
        return render(request, 'templates/brandmanager_login.html')

def pragency_register(request):
    if request.method == 'POST':
        form = PRManagerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = PRManagerRegistrationForm()
    return render(request, 'templates/pragency_register.html', {'form': form})

def pragency_login(request):
    if request.method == 'POST':
        form = PRLoginform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard') # replace with your desired redirect URL after login
            else:
                form.add_error('email', 'Invalid email or password.')
    else:
        form = PRLoginform()
    return render(request, 'templates/pragency_login.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard') # replace with your desired redirect URL after login
            else:
                form.add_error('email', 'Invalid email or password.')
    else:
        form = PRLoginform()
    return render(request, 'admin.html', {'form': form})

    import requests
from requests_oauthlib import OAuth2Session

def influencer_callback(request):
    # Get the authorization code from the request
    code = request.GET.get('code')

    # Set up the OAuth2Session with your client ID and secret
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'
    redirect_uri = 'http://localhost:8000/callback/'
    token_url = 'https://api.third-party-service.com/oauth/token'
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)

    # Exchange the authorization code for an access token
    token = oauth.fetch_token(token_url, code=code, client_secret=client_secret)

    # Store the access token in the database
    # ...

    return redirect('/')

    from requests_oauthlib import OAuth2Session

def influencer_login(request):
    # Set up the OAuth2Session with your client ID and secret
    client_id = 'your_client_id'
    redirect_uri = 'http://localhost:8000/callback/'
    authorization_url = 'https://api.third-party-service.com/oauth/authorize'
    scope = ['read', 'write']
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)

    # Redirect the user to the third-party service's authorization page
    authorization_url, state = oauth.authorization_url(authorization_url)

    return redirect(authorization_url)

