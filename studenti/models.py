from django.db import models
from django.core.validators import RegexValidator
# Modelis DB tabulai, modelis saucas students, tā arī izsaucam citur. Saliek lauku tipus, lai vaicājums nenobeidzas. Ir papildus klase, kurā ieliek tabulas nosaukumu.
class students(models.Model):
    surname = models.CharField(max_length=10,verbose_name="Uzvārds")
    forename = models.CharField(max_length=10,verbose_name="Vārds")
    student_no = models.CharField(max_length=10,verbose_name="Studenta kods",validators=[RegexValidator(r'^[0-9]{8}$')], unique=True)
    aktivs = models.BooleanField(default=True,
        choices=(
            (True, "Aktīvs"),
            (False, "Nav aktīvs"),
        ),verbose_name="Status")
    class Meta:
     db_table = "students"
