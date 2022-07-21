import math
from django.shortcuts import redirect, render
from studenti.forms import studenta_edit_form

from studenti.models import students
from kursi.models import modules
from atzimes.models import marks

# Create your views here.

def index(request):
    visi_studenti = students.objects.all()
    visi_kursi = modules.objects.all()
    visas_atzimes = marks.objects.all()
    for st in visi_studenti:
        summa = 0
        statuss= "Atbilst"
        atzimju_skaits = 0
        for atz in visas_atzimes:
            if atz.student_no == st.student_no:
                summa = summa + atz.mark
                atzimju_skaits = atzimju_skaits +1
                if atz.mark == 0:
                    statuss = "Ir parāds"
                elif atz.mark == "":
                    statuss = "Nav visas atzīmes"
        if atzimju_skaits > 0 :
            st.videjais = math.floor(summa /atzimju_skaits * 10) / 10
            st.statuss = statuss
        else:
            st.videjais = 0
            st.statuss = "Atzīmju nav"
    return render(request, "pages/visi_studenti.html", {"studenti":visi_studenti,"atzimes":visas_atzimes,"kursi":visi_kursi,"title":"Studentu Sākumlapa"})
def labot_studentu(request,studenta_nr=None):
    st = students(student_no=studenta_nr) 
    try:
        st = students.objects.get(student_no=studenta_nr)
    except st.DoesNotExist:   
        pass
    if request.method == 'POST': # ja nospieda pogu un metode ir post
        form = studenta_edit_form(request.POST,instance=st)
        if form.is_valid():
            form.save()
    else:
       form = studenta_edit_form(instance=st)   
    return render(request, "pages/labot_studentu.html", {"form":form,"title":"Labot studentu"})
