from asyncio.windows_events import NULL
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import requests
def sakumlapa(request):
    return render(request, "homepage.html", {"content":" Home","title":"virsraksts"})

def api_tests_universitates(request):
    errors = []
    kontenti = []
    url = NULL
    if request.method == "POST":
        if not request.POST.get("valsts"):
            errors.append("Kļūda! Nav datu")
        else:
            url = 'http://universities.hipolabs.com/search?country='+request.POST.get("valsts")
    else:
        url = 'http://universities.hipolabs.com/search?country=Latvia'
    if url != NULL:
     kontenti = json.loads(requests.get(url).text)
    return render(request, "list.html", {"content":kontenti,"title":"virsraksts","errors":errors})