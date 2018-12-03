"""resolute URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail_view', views.detail_view, name='detail_view'),
    path('locationpost', views.locationpost, name='locationpost'),
    path('table', views.table, name='table'),
    # path('track', views.track, name='track')
    path('check/<slug:slug>/', views.check, name='check'),
    path('collection_check/<int:id>/', views.collection_check, name='collection_check'),
    path('track/<slug:slug>/', views.track, name='track'),
    path('trail/<slug:slug>/', views.trail, name='trail'),
    path('mapping/<slug:slug>/', views.mapping, name='mapping'),
    # path('test', views.test, name='test'),
]
