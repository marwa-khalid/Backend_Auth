from django.shortcuts import render, redirect
from .forms import BrandManagerRegistrationForm

def register(request):
    if request.method == 'POST':
        form = BrandManagerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = BrandManagerRegistrationForm()
    return render(request, 'brandmanagers/register.html', {'form': form})
