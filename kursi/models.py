from django.db import models
from django.core.validators import RegexValidator

# Modelis DB tabulai, modelis saucas modules, tā arī izsaucam citur. Saliek lauku tipus, lai vaicājums nenobeidzas. Ir papildus klase, kurā ieliek tabulas nosaukumu.
class modules(models.Model):
    db_table = "modules"
    module_code = models.CharField(validators=[RegexValidator(r'^[A-Za-z0-9]{6}$')],max_length=10,verbose_name="Kursa kods", unique=True)
    module_name = models.CharField(max_length=50,verbose_name="Kursa nosaukums")
    var_atzimes = models.BooleanField(choices=((True, "Drīkst ievadīt atzīmes"), (False, "Nedrīkst ievadīt atzīmes"),),verbose_name="Atzīmju ievadīšana")
    aktivs = models.BooleanField(choices=((True, "Kurss ir redzams"), (False, "Kurss nav redzams"),),verbose_name="Kurss ir aktīvs")
    class Meta:
     db_table = "modules"
     unique_together = ["id", "module_code"]