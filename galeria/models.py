from django.db import models

import django.utils.timezone

class Fotografia(models.Model):
    
    OPCOES_CATEGORIA = [
        ('ESTRELA','Estrela'),
        ('PLANETA','Planeta'),
        ('BURACO NEGRO','Buraco Negro'),
        ('SATÉLITE','Satélite')
    ]
    
    nome = models.CharField(max_length=50, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length= 60, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/',blank=True)
    publicado = models.BooleanField(default=True)
    horario = models.DateTimeField(default=django.utils.timezone.now, blank=False)

    def __str__(self):
        return self.nome