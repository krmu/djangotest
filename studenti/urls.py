from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name="studenti_index"),
    path('labot/<slug:studenta_nr>', views.labot_studentu,name="studenti_labot"),
    path('labot/', views.labot_studentu,name="studenti_labot"),
    path('visi/', views.skatit_visus,name="studenti_visi"),
]
