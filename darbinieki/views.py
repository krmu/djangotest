from django.shortcuts import render
from darbinieki.forms import Darbinieks_update_form, Jauns_darbinieks_form

from darbinieki.models import User
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required(login_url='/autorizacija/')
@user_passes_test(lambda u: u.admin,login_url='/nav-piekluves/')
def visi_darbinieki(request):
    return render(request, "pages/visi_darbnieki.html", {"darbinieki":User.objects.all(),"title":"Labot vērtējumu"})

@login_required(login_url='/autorizacija/')
@user_passes_test(lambda u: u.admin,login_url='/nav-piekluves/')
def labot_darbinieku(request,darbinieka_id):
    instance = User.objects.get(id=darbinieka_id)
    if request.method == 'POST': # ja nospieda pogu un metode ir post
        form = Darbinieks_update_form(request.POST,instance=instance)
        if form.is_valid():
            form.save()
    else:
        form = Darbinieks_update_form(instance=instance)
    return render(request, "pages/labot_darbinieku.html", {"form":form,"title":"Labot vērtējumu"})

@login_required(login_url='/autorizacija/')
@user_passes_test(lambda u: u.admin,login_url='/nav-piekluves/')
def jauns_darbinieks(request):
    if request.method == 'POST': # ja nospieda pogu un metode ir post
        form = Jauns_darbinieks_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Jauns_darbinieks_form()
    return render(request, "pages/labot_darbinieku.html", {"form":form,"title":"Labot vērtējumu"})