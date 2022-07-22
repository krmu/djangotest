from django.urls import path
from . import views

urlpatterns = [
    path('universitates/meklet/valsts/<valsts>', views.meklet_universitati),
    path('universitates/meklet/valsts/', views.meklet_universitati,name="meklet_uni_api"), # apmānam, lai nav jādomā saite.., lai var izmantot adresi ajaxa funkcijā
]