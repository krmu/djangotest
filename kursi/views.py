from django.shortcuts import redirect, render
from kursi.forms import kursa_edit_form
from django.contrib.auth.decorators import login_required,user_passes_test

from kursi.models import modules

@login_required(login_url='/autorizacija/')
@user_passes_test(lambda u: u.is_staff,login_url='/nav-piekluves/')
def kursi_labot_kursu(request,kursa_id=None):
    kurss = modules(module_code=kursa_id) 
    try:
        kurss = modules.objects.get(module_code=kursa_id)
    except kurss.DoesNotExist:   
        pass
    if request.method == 'POST': # ja nospieda pogu un metode ir post
        form = kursa_edit_form(request.POST,instance=kurss)
        if form.is_valid():
            form.save()
    else:
       form = kursa_edit_form(instance=kurss)   
    return render(request, "pages/labot_kursu.html", {"form":form,"title":"Labot kursu"})

@login_required(login_url='/autorizacija/')
@user_passes_test(lambda u: u.is_staff,login_url='/nav-piekluves/')
def skatit_visus(request):
    return render(request, "pages/skatit_visus_kursi.html", {"data":modules.objects.order_by("module_name").all(),"title":"Visi kursi"})
