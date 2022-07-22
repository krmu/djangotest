from django.shortcuts import render
from atzimes.forms import atzimju_edit_form
from studenti.models import students
from kursi.models import modules
from atzimes.models import marks
from django.contrib.auth.decorators import login_required,user_passes_test



@login_required(login_url='/autorizacija/')
@user_passes_test(lambda u: u.is_staff,login_url='/nav-piekluves/')
def labot_atzimi(request,kursa_id,studenta_kods):
    atzime = marks() 
    try:
        atzime = marks.objects.filter(student_no=studenta_kods).filter(module_code=kursa_id).get()
    except atzime.DoesNotExist:   
        atzime = marks(student_no=studenta_kods,module_code=kursa_id) 
    if request.method == 'POST': # ja nospieda pogu un metode ir post
        form = atzimju_edit_form(request.POST,instance=atzime)
        if form.is_valid():
            form.save()
    else:
       form = atzimju_edit_form(instance=atzime)  
    persona = students.objects.get(student_no=studenta_kods) #Iegūstam personu pēc tā koda
    kurss = modules.objects.get(module_code=kursa_id)    
    return render(request, "pages/labot_atzimi.html", {"form":form,"students":persona,"kurss":kurss,"title":"Labot vērtējumu"})