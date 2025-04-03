from django.contrib import admin
from .models import Pacientes, DadosPaciente, Evolucao

admin.site.register(Pacientes)
admin.site.register(DadosPaciente)
admin.site.register(Evolucao)
