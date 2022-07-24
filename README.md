# Django testa vietne
Django testa vietne, par bāzi ņemta studentu apmācības sistēma.

# Iespējas
    Web - galvenais projekts, visas adreses
    atzimes - Atzīmju modulis. Labošana, dzēšana, pielikšana
    kursi - Kursu modulis. Labošana, dzēšana, pielikšana
    studenti - Studentu modulis. Labošana, dzēšana, pielikšana
        Ja studentam ieliek 0,kas tulkojas kā N, tad status mainās uz "Parāds"
# Adreses: 
    /studenti/ - Tabula ar visiem priekšmetiem un studentiem
    /studenti/labot/<StudentaKods> - Studenta labošanas forma
    /studenti/labot/ - Studenta pielikšanas forma
    /kursi/labot/<KursaKods> Kursa labošanas forma
    /kursi/labot/ Kursa pielikšanas forma
    /api_tests_universitates - Api tests uz universitāšu sarakstu
    /darbinieki/ - Visi sistēmas darbinieki
    /darbinieki/<DarbiniekaId>/labot - Labot darbinieku
    /darbinieki/jauns - Jauns darbinieks
    /api/universitates/meklet/valsts/<valsts> - Apis, kurš meklē HyppoLabs sarakstā visas pieejamās universitātes pēc dotās valsts

Pamatā bija lietots MySQL, var uz citas bāzes likt.
# Tabulas:
    students
        id (int 11)
        student_no (varchar 20)
        surname (varchar 20)
        forename (varchar 20)
        aktivs (int 1)
    modules
        id (int 11)
        module_code varchar(8)
        module_name varchar(50)
        var_atzimes tinyint(1)
        aktivs tinyint(1)
    marks
        id int(11)
        student_no varchar(10)
        module_code	varchar(8)	
        mark int(11)
        last_update timestamp	ON UPDATE CURRENT_TIMESTAMP()	
    darbinieki_user
        id
        password    varchar(128)
        last_login datetime
        username varchar(255)
        is_active bool
        staff bool
        admin bool
        uzvards varchar(255)
        vards varchar(255)
# Info 
    Katrs modulis ir atdalīts atsevišķi. Studenti,kursi, atzīmes. Tā kā ir ņemta jau gatava DB,tad kursi tiek angliski saukti par modules.
    Failos Models glabājas DB lauki. Forms.py glabājas gatavās formas, jo Django ļauj automātiski veidot formas, nav jāveidot lauciņi.
    Formām par pamatu tiek doti Models.py lauki.
    Settingu failu nav, taisiet paši, bet būtībā settingu failā ir veiktas izmaiņas tikai ar DB.

    Ir pielikts arī slavenais Universitāšu API piemēram.
    Viss pamats ir ielikts iekšā web projektā.

    Darbiniekiem divas piekļuves staff un admin.
        staff - var visu izņemot pārvaldīt darbiniekus
        admin - var visu

    Katram skatam klāt ir divi palīgi:
        @login_required(login_url='/autorizacija/') - Šis pasaka, ka vajag autorizēties, ja nē redirektē uz /autorizacija/ - adrese web.urls, kur autorizējas.
        @user_passes_test(lambda u: u.is_staff,login_url='/nav-piekluves/') - pārbauda vai lietotājs ir staff.
#   Svarīgi par stiliem 
    Lai palaistu static mapi ar stiliem utt. https://www.digitalocean.com/community/tutorials/working-with-django-templates-static-files

# Templates
    Galvenais fails - main.html (Iekšā ir viss rāmis, kurā viss tiek ielikts.)
        Pages - lapas, tur ir atsevišķās lapas
        homepage.html - sākumlapa

# Bildes
## Viss kopā
![Viss kopā](/static/img/showcase/viss_kopa.png "Title")
## Jauns students
![Jauns students](/static/img/showcase/jauns_students.png "Title")
## Jauns Kurss
![Jauns Kurss](/static/img/showcase/jauns_kurss.png "Title")
## Atzīmju ievade
![Jauns students](/static/img/showcase/labot_atzimi.png "Title")


# Kā to visu palaist

1. Atveram mapi,kur viss glabāsies, Django ir daudz failu..
2. `python -m pip install Django` Instalējam Django
3. `django-admin startproject web` Izveidojam jauun projektu, sauktu par Web.
4. Web mapes saturu aizvietojam ar šo projektu. Ja jūtas advancēts, drīkst arī izmantot `git` komandas.
5. Konsolē python manage.py createsuperuser

# Login sistēma

Par login sistēmas pamatu ņemts:  https://www.codingforentrepreneurs.com/blog/how-to-create-a-custom-django-user-model/

Lai uztaisītu jaunu superlietotāju - python manage.py createsuperuser


# API

Adrese ir /api/
Lai darbotos vajag izmantot
data: { 
    csrfmiddlewaretoken: "{{ csrf_token }}",
},
CSRF tokens, kuru izmanto uz POST metodēm, pats Django pārbauda, ja neder atbild ar 403.


# Ja laiž uz servera ar Apache

Apachei vajag moduli - libapache2-mod-wsgi-py3, to instalē `sudo apt-get install libapache2-mod-wsgi-py3`
Tad labojam failu, kurā dzīvo weba konfigurācija jeb `/etc/apache2/sites-available/000-default.conf`
Tur jāpieliek šādas rindas:

WSGIScriptAlias / /var/www/web/web/wsgi.py # Mūsu servera faila pamata moduļa atrašanās vieta sk. šo pašu projektu.

Sakām, ka mūsu galvenais modulis ir tas,kurš darbina wsgi.py failus, ļaujam izmantot failus
`<Directory /var/www/web/web>
    <Files wsgi.py>
        Order deny,allow
        Allow from all
    </Files>
</Directory>`

Pieliekam klāt stila failu mapi, lai saucot adresi /static/ tiktu izsaukta mūsu iekšēja stilu mape. 

`Alias /static/ "/var/www/web/static/"
<Directory "/var/www/web/static">
Require all granted
</Directory>`

Mapē /web/web/wsgi.py failā pieliek klāt rindas.
import sys
sys.path.append('/var/www/web')
sys.path.append('/var/www/web/web')
Pasakām, kur projekts dzīvo.

Svarīgi:

Datubāzes failam jānorāda pilns ceļš, ja lieto sqllite.
Views.py izkomentējam ārā rindu #from asyncio.windows_events import NULL tā raisa problēmu, ja darbojas ar linux vidi.

# Testēts šādās vidēs

Windows 11
DigitalOcean [1]
    1 GB Memory
    25 GB Disk
    Debian 11 x64
DigitalOcean [2]
    512 MB  Memory
    10 GB Disk
    Debian 11 x64