from django.forms import HiddenInput, ModelForm
from .models import marks

class atzimju_edit_form(ModelForm):
   def __init__(self, *args, **kwargs):
        super(atzimju_edit_form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
   class Meta:
        model = marks
        fields = ['mark','module_code','student_no']
        widgets = {'module_code': HiddenInput(),'student_no': HiddenInput()}
        