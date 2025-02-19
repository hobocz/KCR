"""
URL configuration for bb_analytics project.

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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('players/', include('player_data.urls')),
]

[
    {
        "id": 671096,
        "name_first": "Andrew",
        "name_use": "Andrew",
        "stats": {
            "batting": [],
            "pitching": [
                {
                    "year": 2024,
                    "league": "NL"
                }
            ]
        }
    },
    {
        "id": 671097,
        "name_first": "Bob",
        "name_use": "Andrew",
        "stats": {
            "batting": [],
            "pitching": [
                {
                    "year": 2023,
                    "league": "AL"
                }
            ]
        }
    }
]