# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Hosts(models.Model):
    host_name 	= models.CharField('Host', max_length=100)
    ip 			= models.CharField('IP', max_length=255)
    port 		= models.CharField('Porta', max_length=6)

    active 		= models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Host'
        verbose_name_plural = 'Hosts'
        ordering = ['ip']
