from django.db import models
from django.db.models.fields import CharField

class Tarefa(models.Model):
    OPCOES_STATUS = (
        ('concluído', 'Concluído'),
        ('pendente', 'Pendente'),
        ('adiado', 'Adiado')
    )

    OPCOES_CATEGORIAS = (
        ('urgente', 'Urgente'),
        ('importante', "Importante"),
        ('atencao', 'Atenção'),
    )

    descricao = models.CharField(max_length=400)
    criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=25, choices=OPCOES_CATEGORIAS,
                                default='importante')
    status = models.CharField(max_length=25, choices=OPCOES_STATUS,
                            default='pendente')
