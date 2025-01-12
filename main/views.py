from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('../Frontend/html/profile.html')  # Adjust if you have a specific profile page
    else:
        form = AuthenticationForm()
    return render(request, '../Frontend/html/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('../Frontend/homepage.html')  # Adjust to your desired redirect page
