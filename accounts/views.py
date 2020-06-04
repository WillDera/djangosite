from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def signup_view(request):
    
    # check if request is a POST
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        # verify if the inputs are valid and also,
        # check if user already exists
        if form.is_valid():
            form.save()
            # log user in
            return redirect('djangoblog:article')
    else:
        # create new instance of the UserCreationForm
        form = UserCreationForm()

    # the 3rd param in render is the data being passed down to 
    # the template "signup.html"
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log user in
            return redirect('djangoblog:article')
    else:
        form = AuthenticationForm
    return render(request, 'accounts/login.html', {'form':form})