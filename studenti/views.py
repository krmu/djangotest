from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import redirect, render
from studenti.forms import studenta_edit_form

from studenti.models import students
from kursi.models import modules
from atzimes.models import marks

# Create your views here.
@login_required(login_url='/autorizacija/')
@user_passes_test(lambda u: u.is_staff,login_url='/nav-piekluves/')
def index(request):
    visi_kursi = modules.objects.all()
    dati = []
    studenta_dati = {}
    for st in students.objects.all():
        studenta_dati = {"ID":st.id,"vards":st.surname,"uzvards":st.forename,"uzvards":st.forename,"aktivs":st.aktivs,"kods":st.student_no,"kursu_dati":{},"papildus_info":[]}
        summa = 0
        vertejumi = 0
        statuss = "Atbilst"
        for kurss in visi_kursi:
            vertejums = None
            try:
                vertejums = marks.objects.get(student_no=st.student_no,module_code=kurss.module_code)
            except marks.DoesNotExist:   
                pass # mums baigi neinteresē iznākums.
            if vertejums is not None and kurss.aktivs and kurss.var_atzimes:
                summa = vertejums.mark + summa
                vertejumi = vertejumi + 1
                if vertejums.mark == 0 and statuss == "Atbilst":
                    statuss = "Parāds"
            studenta_dati['kursu_dati'][kurss.module_code] = {"atzime":vertejums}
        if vertejumi == 0:
            vertejumi = 1 # tiem, kuriem nav atzīmju
        studenta_dati['papildus_info'] = {"videjais": format(summa/vertejumi, '.2f'),"status":statuss}
        dati.append(studenta_dati)
    #return print(dati)
    return render(request, "pages/visi_studenti.html", {"dati":dati,"kursi":visi_kursi,"title":"Studentu Sākumlapa"})
@login_required(login_url='/autorizacija/')
@user_passes_test(lambda u: u.is_staff,login_url='/nav-piekluves/')
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

@login_required(login_url='/autorizacija/')
@user_passes_test(lambda u: u.is_staff,login_url='/nav-piekluves/')
def skatit_visus(request):  
    return render(request, "pages/skatit_visus_studenti.html", {"data":students.objects.order_by("surname").all(),"title":"Skatīt visus"})
