from django.urls import path
from . import views


urlpatterns = [
    path('', views.visi_darbinieki,name="visi_darbinieki"),
    path('<slug:darbinieka_id>/labot', views.labot_darbinieku,name="darbinieku_labot"),
    path('jauns', views.jauns_darbinieks,name="jauns_darbinieks")
]
