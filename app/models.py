from django.db import models

class Serie(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Série")
    estreia = models.CharField(max_length=4, verbose_name="Ano de Estreia")
    genero = models.CharField(max_length=200, verbose_name="Gênero")
    publico = models.CharField(max_length=100, verbose_name="Público-alvo")
    estilo = models.CharField(max_length=255, verbose_name="Estilo")

    class Meta:
        verbose_name = "Série"
        verbose_name_plural = "Séries"

    def __str__(self):
        return self.nome

class Personagem(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    idade = models.IntegerField(verbose_name="Idade")
    posicao = models.CharField(max_length=100, verbose_name="Posição")
    local = models.CharField(max_length=100, verbose_name="Local")
    imagem = models.ImageField(upload_to='personagens/', verbose_name="Imagem")

    class Meta:
        verbose_name = "Personagem"
        verbose_name_plural = "Personagens"
        ordering = ['nome']

    def __str__(self):
        return self.nome

class SobreInfo(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título")
    objetivo = models.TextField(verbose_name="Objetivo")
    projeto = models.TextField(verbose_name="Sobre o Projeto")
    tecnologias = models.CharField(max_length=200, verbose_name="Tecnologias Utilizadas")
    desenvolvedora = models.CharField(max_length=100, verbose_name="Desenvolvedora")
    instituicao = models.CharField(max_length=255, verbose_name="Instituição")
    ano = models.CharField(max_length=4, verbose_name="Ano")

    class Meta:
        verbose_name = "Informação Sobre"
        verbose_name_plural = "Informações Sobre"

    def __str__(self):
        return self.titulo

