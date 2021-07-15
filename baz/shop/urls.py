from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Shopindex"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="tracker"),
    path("products/", views.product, name="products"),
    path("search/", views.search, name="search"),


]