from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    pass

# Login View
def login(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username= username, password=password)

        if user is not None:
            return HttpResponseRedirect(reverse("index"))
        else:
            # Display a message to the user detailing they have not pass authentication
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "home/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
