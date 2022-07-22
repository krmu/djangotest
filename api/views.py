from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import render
import requests

# Create your views here.

def meklet_universitati(request,valsts):
    if request.method == 'POST':
        atbilde = {}
        if valsts is None:
            atbilde.error= "Trūkst parametru" # ja gadījumā apgāja mūsu gudro javascript IF nosacījumu.
        else:
            atbilde = requests.get("http://universities.hipolabs.com/search?country="+valsts).text # mums neinteresē kas tiek atdots, to nodrošina serviss
        return JsonResponse(atbilde, safe=False) # atdodam.
    else:
       return HttpResponseForbidden() # Nosūta 403, jo gribam tikai POST metodes.