#!/usr/bin/python3
#-*- coding: utf-8 -*-
import sys

def checkType(objet1):
    print("le type d'objet est ",type(objet1),"et la valeur est=",objet1)


#LIST=> ordonée , indexée
a=[",tomate","salade","mirabelle","pommedeterre"]
b=["janvier","fevrier","mars","avril"]
b2=b
b3=list(b)
extra=["mai","juin","juillet"]
#TUPLE
c=("une","deux","trois","quatre")

#SET
d={"janvier","fevrier","mars","avril"}


print("le première mos de l'année est=",b[0])

#LIST
for i in b:
    print("la liste contien l'info suivante",i)
#AJOUTER ELEMNTS À LA LISTE
b.append("mai")
taillelist=len(b)
print("la taille de la liste est ",taillelist)
checkType(b)
checkType("mai")
checkType(["mai","juin"])


for i in b:
    print("la liste contien l'info suivante",i)

for i in b2:
    print("la liste2 contien l'info suivante",i)
for i in b3:
    print("la liste3 contien l'info suivante",i)
b3+=extra
for i in b3:
    print("la liste3 CONCATENE contien l'info suivante",i)


for i in c:
    print("le tuple contient l'info suivante ",i)

for i in d:
    print("le set contient l'info suivante ",i)
    