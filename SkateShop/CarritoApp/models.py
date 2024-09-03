
from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    IntegerField,
    ImageField,
    CASCADE
)
from django.contrib.auth.models import User

# Create your models here.
class Producto(Model):
    nombre = CharField(max_length=64, null= False, unique=True)
    categoria = CharField(max_length=25)
    precio = IntegerField()
    imagen = ImageField(upload_to='productos/', null=True)
    usuario = ForeignKey(User, on_delete= CASCADE)


    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
    
    def imagen_url(self):
        if self.imagen and hasattr(self.imagen, 'url'):
            return self.imagen.url
        else:
            return ''
 
