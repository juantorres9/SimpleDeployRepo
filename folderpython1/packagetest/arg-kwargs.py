#!/usr/bin/python3
#-*- coding: utf-8 -*-
import sys


def displayKwargsNow(**kwargus):
    print("la variable kwargus vaut ",kwargus,"est de type ",type(kwargus),"est de taile ",len(kwargus))
    for key,value in kwargus.items():
        print("le key est",key,"le values est=",value,"de type type(value)",type(value))
    
    #**KWARGS : principe utilisé pour passer une nombre infinite des parametres avec key=value syntax 




kwags_var={'resp1':1,'resp2':2,'resp3':3,5:500}

displayKwargsNow(resp1=1,resp2=2,resp3=3,resp4="numero4")


