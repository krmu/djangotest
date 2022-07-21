from django.forms import ModelForm
from .models import modules

class kursa_edit_form(ModelForm):
   def __init__(self, *args, **kwargs):
        super(kursa_edit_form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
   class Meta:
        model = modules
        fields = '__all__'
        