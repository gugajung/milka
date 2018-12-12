from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Vendedores(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome_cliente = models.CharField(max_length=30)

class Atendimento(models.Model):
    SITUACAO_CHOICES = (
        ('AB', 'Aberto'), ('AT', 'Em Atendimento'),
        ('NF', 'Negócio Fechado'), ('NR', 'Negócio não Realizado'))
    cliente = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    situacao = models.CharField(max_length=50, choices=SITUACAO_CHOICES)
    data = models.DateField(auto_now=True, editable=False)
    observacoes = models.TextField(max_length=500, blank=True, null=True,
                                   verbose_name='Observações', help_text='500 caracteres no máximo')

    def __str__(self):
        return self.situacao + ' - ' + self.cliente.nome_cliente


class Visita(models.Model):
    atendimento = models.ForeignKey(Atendimento, null=True,on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now,
                            help_text='dd/mm/aaa', verbose_name='Data')
    observacoes = models.TextField(max_length=500, verbose_name="Observações",
                                   blank=True, null=True, help_text='500 caracteres no máximo')

