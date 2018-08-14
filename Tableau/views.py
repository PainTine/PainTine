# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from models import *
# Create your views here.
def accueil(request):
	peinture_data = get_list_or_404(Tableau)
	peinture_dropone=[]
	peinture_droptwo=[]
	peinture_dropthree=[]
	nb=1
	for elem in peinture_data:
		if nb==1:
			peinture_dropone.append(elem)
		elif nb==2:
			peinture_droptwo.append(elem)
		elif nb==3:
			peinture_dropthree.append(elem)
			nb=0
		nb=nb+1
	return render(request, 'index.html', {
											'peinture_dropone':peinture_dropone,
											'peinture_droptwo':peinture_droptwo,
											'peinture_dropthree':peinture_dropthree,
		})
def TableauxView(request, tableau):
	peinture_data = get_list_or_404(Tableau, RealName=tableau)[0]
	Nature_Desc = get_list_or_404(Technique, Nature=peinture_data.Nature)[0]
	return render(request, 'Paints.html', {
				'peinture_data' : peinture_data,
				'Nature_Desc':Nature_Desc,
		})
			