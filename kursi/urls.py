from django.urls import path
from . import views


urlpatterns = [
    path('labot/<slug:kursa_id>', views.kursi_labot_kursu,name="kursi_labot_kursu"),
    path('labot/', views.kursi_labot_kursu,name="kursi_labot_kursu"),
    path('skatit_visus/', views.skatit_visus,name="visi_kursi")
]