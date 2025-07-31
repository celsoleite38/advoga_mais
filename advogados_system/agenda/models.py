from django.db import models
from processos.models import Processo
from clientes.models import Cliente
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

TIPOS_AUDIENCIA = [
    ('forum', '🧑‍⚖️ Audiência Fórum'),
    ('virtual', '💻 Audiência Virtual'),
    ('atendimento', '📞 Atendimento'),
    ('sessao', '⚖️ Sessão de Julgamento'),
    ('conciliacao', '🤝 Mediação / Conciliação'),
    ('reuniao', '📋 Reunião Estratégica'),
]

class Audiencia(models.Model):
    processo = models.ForeignKey(
        Processo, 
        on_delete=models.CASCADE, 
        null=True,    # Permite que o campo seja nulo no banco de dados
        blank=True,   # Permite que o campo seja vazio nos formulários
        related_name="audiencias"
    )
    
    # 3. ADICIONE O CAMPO CLIENTE, TAMBÉM OPCIONAL
    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE, 
        null=True,    # Permite que o campo seja nulo
        blank=True,   # Permite que o campo seja vazio
        related_name="audiencias"
    )
    data_hora = models.DateTimeField()
    tipo = models.CharField(max_length=50, choices=TIPOS_AUDIENCIA)
    local = models.CharField(max_length=200)
    vara = models.CharField(max_length=200, default='Não informado')
    resultado = models.TextField(blank=True)
    
    def clean(self):
        # Garante que ou o processo ou o cliente foi preenchido, mas não ambos.
        if self.processo and self.cliente:
            raise ValidationError('Uma audiência/compromisso deve estar ligada a um Processo OU a um Cliente, não a ambos.')
        if not self.processo and not self.cliente:
            raise ValidationError('Uma audiência/compromisso precisa estar ligada a um Processo ou a um Cliente.')

    def __str__(self):
        # Atualiza o __str__ para lidar com os dois casos
        if self.processo:
            return f'{self.get_tipo_display()} - Proc. {self.processo.numero}'
        elif self.cliente:
            return f'{self.get_tipo_display()} - Cliente {self.cliente.nome}'
        return f'{self.get_tipo_display()} em {self.data_hora.strftime("%d/%m/%Y %H:%M")}'

class LogAudiencia(models.Model):
    audiencia = models.ForeignKey(Audiencia, on_delete=models.CASCADE)
    alterado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    data_anterior = models.DateTimeField()
    nova_data = models.DateTimeField()
    data_alteracao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Audiência #{self.audiencia.id} reagendada por {self.alterado_por}'
