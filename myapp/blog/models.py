from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'

class Autor(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Livro(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    isbn = models.CharField(max_length=13, unique=True)
    publicacao = models.DateField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.IntegerField()
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor, through='Publica')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

class Publica(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'
        unique_together = ['livro', 'autor']  # Garante que não haja duplicatas de livro-autor
