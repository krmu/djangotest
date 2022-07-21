from django.urls import path
from . import views

# Izveido adresi
# Formāts KursaID/StudentaId/labot
# tiek izsaukts skats no faila views.py, tur atrod funkciju ar nosaukumu "labot_atzimi"

urlpatterns = [
    path('<slug:kursa_id>/<int:studenta_kods>/labot', views.labot_atzimi,name="studenti_labot_atzimi"),
]