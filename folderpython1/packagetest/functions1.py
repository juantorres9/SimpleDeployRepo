#!/usr/bin/python3
#-*- coding: utf-8 -*-
import sys

#FONCTIONS AVEC ARGUMENTS MULTYPLES
def displayManyStrings(*argu):    
    print("les parametres sont:",argu,"avec une taille",len(argu),"objet de type",type(argu) )

#FONCTIONS AVEC DEUX PARAMETRES POSITIONNELS
def display2parameters(param1,param2):
    tup1=(param1,param2)
    for i in tup1:
        print ("les parametres valent",i)
    return tup1        

#FONCTION AVEC PLUSIEURS PARAMETRES >= 0 PARAMETRE
displayManyStrings("hola",1)
displayManyStrings("salut")
displayManyStrings()

#FONCTION POSITIONNEL
var1=display2parameters(4, "maisons")
print("le type de la reponse vaut",type(var1))

#var1=display2parameters("choco", )