from django.forms import ModelForm

from backoffice.models import Crud


class CrudForm(ModelForm):
    class Meta:
        model = Crud
        fields = ['codigo', 'nombre', 'foranea', 'entero', 'choice']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
