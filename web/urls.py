from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.sakumlapa,name="sakumlapa"),
    path('api_tests_universitates', views.api_tests_universitates,name="apitest_universitates"),
    path('studenti/', include('studenti.urls')),
    path('atzimes/', include('atzimes.urls')),
    path('kursi/', include('kursi.urls')),
]
