from django.shortcuts import redirect, render
from kursi.forms import kursa_edit_form

from kursi.models import modules

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
    return render(request, "pages/labot_kursu.html", {"form":form,"title":"Labot vērtējumu"})
