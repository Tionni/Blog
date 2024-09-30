from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """Register a new user"""
    if request.method != 'POST':
        #Dispal blank registration form
        form = UserCreationForm()
    else:
        #process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #log the new user and then redirect to the index
            login(request, new_user)
            return redirect('blogs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)