from django.db import models
import datetime
from django.core.validators import MaxValueValidator


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['id']


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField(default=current_year(),
                                       validators=[max_value_current_year, ],
                                       blank=True,
                                       null=True,
                                       db_index=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name='titles')
    genre = models.ManyToManyField(Genre)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
