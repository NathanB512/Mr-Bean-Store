from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def menBrand_view(request):
    return HttpResponseRedirect(reverse("categories/menBrand.html"))


@login_required(login_url='login')
def menCatgeory_view(request):
    return HttpResponseRedirect(reverse("categories/menCategory.html"))


@login_required(login_url='login')
def womenBrand_view(request):
    return HttpResponseRedirect(reverse("categories/womenBrand.html"))


@login_required(login_url='login')
def womenCategory_view(request):
    return HttpResponseRedirect(reverse("categories/womenCategory.html"))
