from django.contrib import admin
from .models import Pessoa, Visita, Vendedores, Atendimento

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Vendedores)
admin.site.register(Atendimento)
admin.site.register(Visita)