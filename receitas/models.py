from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):  # coloca o nome correto no site "admin" da categoria
        return (self.name)


class Recipe(models.Model):
    # criasse o campo "title" do tipo VarChar com 65
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()  # funciona como indice mas tem mais coisa
    preparation_time = models.IntegerField()  # campo numerico
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()  # artigo livre
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True)  # gera data automaticamente
    updated_at = models.DateTimeField(auto_now=True)  # gera a atualização
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
