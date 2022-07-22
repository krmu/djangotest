from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.sakumlapa,name="sakumlapa"),
    path('api_tests_universitates', views.api_tests_universitates,name="apitest_universitates"),
    path('studenti/', include('studenti.urls')),
    path('atzimes/', include('atzimes.urls')),
    path('kursi/', include('kursi.urls')),
    path('darbinieki/', include('darbinieki.urls')),
    path('api/', include('api.urls')),
    path('autorizacija/', views.login,name="login"),
    path('izrakstities/', views.iziet,name="iziet"),
    path('nav-piekluves/', views.nav_piekluves,name="navaccess"),
]
