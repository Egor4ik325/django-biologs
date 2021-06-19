from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import Http404

# Create your views here.

# No view created for login (Django default)

def register(request):
    """ Custom user registration (needs to implement logic with the registered user).
    Can be called to GET web site/inteface/file or to POST form data.  """
    if request.method == 'GET':
        # Use Django built-in form for registering new users
        form = UserCreationForm()
        # Send form to the template
        context = {'form': form}
        return render(request, 'registration/register.html', context)
    elif request.method == 'POST':
        filled_form = UserCreationForm(request.POST)
        if filled_form.is_valid():
            # CUSTOM USER REGISTRATION LOGIC
            # get the created user
            registered_user = filled_form.save()
            # logic registered user (as django.contrib.auth.models.User)
            login(request, registered_user)
            return redirect('biologs:home') # redirect to URL
        else:
            # Send invalid form message
            context = {'form': filled_form}
            return render(request, 'registration/register.html', context)
    else:
        raise Http404

def account(request):
    """ Responds with account web page. """
    return render(request, 'registration/account.html')
