from django.db import models

# Modelis DB tabulai, modelis saucas marks, tā arī izsaucam citur. Saliek lauku tipus, lai vaicājums nenobeidzas. Ir papildus klase, kurā ieliek tabulas nosaukumu.

class marks(models.Model):
    student_no = models.CharField(max_length=10)
    module_code = models.CharField(max_length=8)
    mark = models.IntegerField(
        choices=(
            (0, "NP"),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10)
        ),
        verbose_name="Atzīme"
    )

    class Meta:
     db_table = "marks"