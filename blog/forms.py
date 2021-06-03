from django.forms import ModelForm
from blog.models import Contacto


class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'mensaje']

        error_messages = {
            'nombre':{
                'required': ("Este campo es necesario"),
            },
            'email':{
                'required': ("Este campo es necesario"),
            },
            'mensaje':{
                'required': ("Este campo es necesario"),
            },
        }

        def __init__(self, *args, **kwargs):
            super(ContactoForm, self).__init__(*args, **kwargs)



