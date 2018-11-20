# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect

from models import Hosts
from master.server.forms import HostForm

from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os.path

import json
import requests
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from threading import Thread
import multiprocessing
import pusher
from os.path import join, dirname

pusher_client = pusher.Pusher(
  app_id='652059',
  key='f8dca6cc86dc0ff772f8',
  secret='020c5721ffa64f199c65',
  cluster='us2',
  ssl=True
)


workerCount = 0
# Create your views here.

def index(request):
    #return HttpResponse("Olá MySite")
    template = loader.get_template('frontend/index.html')
    context = {
        'data': [],
    }
    return HttpResponse(template.render(context, request))


def search(request):
    template = loader.get_template('frontend/processing.html')
    


    myfile = request.FILES['file_']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    #uploaded_file_url =os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + fs.url(filename)
    uploaded_file_url =  fs.url(filename)
    
    module_dir = "/Users/renanxavier/Documents/django/master" +fs.url(filename) # get current directory

    word_counter = 0
    word_list = {}
    number_slaves = Hosts.objects.filter(active=True).count() #Pega total de hosts ativos
    with open(module_dir,'r') as fh:
        for line in fh: #Nesse ponto ele já pega cada LINE individualmente
            for word in line.split(): # Aque é para ele pegar cada WORD indivudualmente
                word_list[word_counter] = word # Lista com todas as palavras do arquivo
                word_counter = word_counter + 1  # Conta a quantidade de palavras do arquivo
    #print("AQUi",word_counter)
    number_words_per_slave = word_counter//number_slaves
    slaves = [[0 for x in range(number_words_per_slave)] for y in range(number_slaves)]
    count = 0
    # print("Numero de slaves:",number_slaves)
    #print("Numero de palavras pos slave,",number_words_per_slave)
    for slave in range(number_slaves):
        if slave == (number_slaves-1):
            mod = number_words_per_slave % 2
            if mod != 0:
                print(number_words_per_slave)
                number_words_per_slave = number_words_per_slave + mod
                #print(number_words_per_slave)
        for word in range(number_words_per_slave-1):
            slaves[slave][word] = word_list[count]
            #print(slaves[slave][word])
            count+=1



    h = Hosts.objects.filter(active=True)
    c = 0
    for hos in h:
        payload = {
            "params": [{'words': slaves[c], 'keys': request.POST.get("searchs", "")}]
        }
        c+=1
        Thread(target=worker, args=[hos.ip, hos.port, payload]).start()


    context = {'keys': request.POST.get("searchs", "").split(", ")}

    return HttpResponse(template.render(context, request))

def worker(ip, port, payload):
    url = "http://"+ip+":"+port+"/jsonrpc"
    headers = {'content-type': 'application/json'}

    time.sleep(3)
    try:
        request = requests.post(url, data=json.dumps(payload), headers=headers, timeout=2).json()
        pusher_client.trigger('serach', 'worker', {'message': request})
    except requests.exceptions.RequestException as e:
        print ("erro: ")

        



def dashboard(request):
    #return HttpResponse("Olá MySite")
    template = loader.get_template('backend/index.html')
    hosts = Hosts.objects.all()
    context = {
        'data': [],
        'hosts': hosts,
    }

    return HttpResponse(template.render(context, request))


def createHost(request):
    if request.method == "POST":  
        form = HostForm(request.POST)  
        form.save()
    
    return redirect('dashboard')

def deleteHost(self, pk):
    Hosts.objects.filter(id=pk).delete()
    
    return redirect('dashboard')


def activeHost(self, pk):
    host = Hosts.objects.filter(id=pk)

    if host[0].active == True:
        Hosts.objects.filter(id=pk).update(active = False)
    else:
        Hosts.objects.filter(id=pk).update(active = True)
    
    return redirect('dashboard')


