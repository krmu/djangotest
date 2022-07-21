from django.db import models
from django.core.validators import RegexValidator

# Modelis DB tabulai, modelis saucas modules, tā arī izsaucam citur. Saliek lauku tipus, lai vaicājums nenobeidzas. Ir papildus klase, kurā ieliek tabulas nosaukumu.
class modules(models.Model):
    db_table = "modules"
    module_code = models.CharField(validators=[RegexValidator(r'^[A-Za-z0-9]{6}$')],max_length=10,verbose_name="Kursa kods")
    module_name = models.CharField(max_length=50,verbose_name="Kursa nosaukums")
    class Meta:
     db_table = "modules"