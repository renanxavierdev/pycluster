# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from models import Hosts
#from django.contrib.auth.forms import ProductsCreationForm

#from django.core.exceptions import ValidationError


class HostForm(forms.ModelForm):

    class Meta:
        model = Hosts
        fields = ['host_name', 'ip', 'port']
