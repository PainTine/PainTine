# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import os
from uuid import uuid4

# Create your models here.
def path_and_rename(instance, filename):
    upload_to='Tableau/static/pictures'
    ext = "png"
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

# Create your models here.
MEDIUM = (
		('Aquarelle', 'Aquarelle'),
	    ('Craie', 'Craie'),
	    ('Crayon de couleur', 'Crayon de couleur'),
	    ('Encaustique', 'Encaustique'),
	    ('Encre', 'Encre'),
	    ('Gouache', 'Gouache'),
	    ('Pastel secs et Crayon pastel', 'Pastel secs et Crayon pastel'),
	    ('Pastels gras', 'Pastels gras'),
	    ('Peinture acrylique', 'Peinture acrylique'),
	    ('Peinture à l\'huile', 'Peinture à l\'huile'),
	    ('Huile solide', 'Huile solide'),
	    ('Pigments', 'Pigments'),
	    ('Sanguine', 'Sanguine'),
	    ('Feutre', 'Feutre'),
	    ('Tempera', 'Tempera'),
	    ('Crayon graphite', 'Crayon graphite'),
	    ('Encre de Chine', 'Encre de Chine'),
	    ('Fusain', 'Fusain'),
	    ('Mine de plomb', 'Mine de plomb'),
	    ('Pierre noire', 'Pierre noire'),
	    ('Pointe d\'argent', 'Pointe d\'argent'),
	)
REAL = (
	('Morgane Carluer', 'Morgane Carluer'),
	('Christine Carluer', 'Christine Carluer'),
	)

class Technique(models.Model):
	"""docstring for Nature"""
	Nature = models.CharField(max_length=30, choices=MEDIUM, unique=True)
	Description = models.CharField(max_length=500, default='')

	def __str__(self):
		return self.Nature
	class Meta:
		ordering = ('Nature',)

class Tableau(models.Model):
	RealName = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
	Nom = models.CharField(default='', max_length=30)
	Longueur = models.CharField(default='', max_length=3)
	Largueur = models.CharField(default='', max_length=3)
	Nature = models.ForeignKey(Technique, on_delete=models.CASCADE)
	Image = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)
	Realisateur = models.CharField(max_length=30, choices=REAL)
	def __str__(self):
		return self.Nom + ' - ' + self.Realisateur + ' - ' + self.Longueur + ' - ' + self.Largueur