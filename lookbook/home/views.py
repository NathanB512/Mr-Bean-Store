from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    return HttpResponse("Goodbye Son")

# Login View
def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            # Display a message to the user detailing they have not pass authentication
            return render(request, "home/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "home/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
