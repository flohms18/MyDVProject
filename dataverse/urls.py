"""
URL configuration for MyDVProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.urls import path, include

from . import views
from dataverse.views import datarole_detail
from dataverse.views import article_detail


urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("datarole", views.datarole, name="datarole"),
    path("glossary", views.glossary, name="glossary"),
    path("governance", views.governance, name="governance"),
    path("datarole/<int:data_role_id>/", datarole_detail, name="datarole_detail"),
    path("article/<int:article_id>/", article_detail, name="article_detail"),
    path("tinymce/", include("tinymce.urls")), 

    
]

