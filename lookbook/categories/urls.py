from django.urls import path
from . import views

urlpatterns = [
    path("men/brand", views.menBrand_view, name="menBrand"),
    path("men/brand", views.menCategory_view, name="menCategory"),
    path("men/brand", views.womenBrand_view, name="womenBrand"),
    path("men/brand", views.womenCategory_view, name="womenCategory"),
]
