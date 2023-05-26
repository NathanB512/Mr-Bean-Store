from django.urls import path
from . import views

urlpatterns = [
    path("men/brand", views.menBrand_view, name="menBrand"),
    path("men/category", views.menCategory_view, name="menCategory"),
    path("women/brand", views.womenBrand_view, name="womenBrand"),
    path("women/category", views.womenCategory_view, name="womenCategory"),
]
