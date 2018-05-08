from django.contrib import admin
from apps.configurarSimulacion.models import *

# Register your models here.
admin.site.register(Siembra)
admin.site.register(Configuracion)
admin.site.register(FaseCultivo)
admin.site.register(Simulacion)
admin.site.register(Usuario)