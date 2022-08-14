# Createur < Doc.Shaka >

# -*- coding: utf-8 -*-

# Installation des Librairy

import os
from os import *

system("pip install art")
system("pip install termcolor")
system("cls")


# Librairy utilisé

from art import *
from termcolor import colored 


  
def main(): # Début de def main

    # Pixel art

    print()

    print(colored(text2art ("\t___________________\n"),'yellow'))
    print(colored(text2art ("\t__Recettes_d'Autant__"),'blue'))
    print(colored(text2art ("\t___________________"),'yellow'))

    print()

    # Code python pure

    print ("\t[ Tables des Matiéres ]")

    print()

    print ("\t<< 1 . [gateaux_aux_chocolat] >>")

    print()

    print ("\t<< 2. [gateaux_aux_yaourt] >>")

    print()

    print ("\t<< 3. [crepes] >>")

    print ()

    choix = input("\tRecette > ")

    #choix des recettes et affichages des proportions demandé par rapport au nb de personne

    if choix == "gateaux_aux_chocolat":

        # le gateaux aux chocalat pour 4 personne : 2 oeufs , 133.5 gr de chocolats , 66.5 g de beurre , 33.5 g de farine , 66.5 g de sucre en poudre

        print ()

        print ("\tRecette du gateaux au chocolat ")

        print ()

        inv=int(input("\tRecette 1 > Pour combien de personnes ?"))

        print ()

        print ("\tRecette 1 > Pour" ,inv ,"personne, il vous faudra :")

        print ()

        print ("\t-" ,2/4*inv ,"oeufs")

        print ("\t-" ,133.5/4*inv ,"grammes de chocolat patissier")

        print ("\t-",66.5/4*inv ,"grammes de beurre")

        print ("\t-",33.5/4*inv ,"grammes de farine")

        print ("\t-",66.5/4*inv ,"grammes de sucre en poudre")

        print ()

        print ("\tRecette 1 > le temps de préparation sera de 40 minutes")

        print ()

        print ("\tRecette 1 > Bonnne appétit à vous !!")

        print ()

    elif choix == "gateaux_aux_yaourt":

        # Le gateaux aux yaourth pour 4 personne : 2 oeufs , 0.5 paquet de levure chimique , 0.5 pots d'huile , 3 pots de farine , 2 pots de sucre semoule , 1 zeste de citron jaune , 
        # 1 pot de yaourt nature 

        print ()

        print ("\tRecette du gateaux aux yaourt ")

        print ()

        inv=int(input("\tRecette 2 > Pour combien de personnes ?"))

        print ()

        print ("\tRecette 2 > Pour" ,inv ,"personne, il vous faudra :")

        print ()

        print ("\t-" ,2/4*inv ,"oeufs")

        print ("\t-" ,0.5/4*inv ,"paquet de levure chimique")

        print ("\t-",0.5/4*inv ,"port de d'huile")

        print ("\t-",3/4*inv ,"pots de farine")

        print ("\t-",2/4*inv ,"pots de sucre semoule")

        print ("\t-",1/4*inv ,"zeste de citron")

        print ("\t-",1/4*inv ,"yaourts")

        print ()

        print ("\tRecette 2 > le temps de préparation sera de 45 minutes")

        print ()

        print ("\tRecette 2 > Bonnne appétit à vous !!")

        print ()

    elif choix == "crepes":

        # Le recette des crépes pour 4 personne : 4 oeufs , 1 pincée de sel , 1/2 l de lait , 250 gr farine , 2 cuilliére a soupe de sucre, 50 g de beurre

        print ()

        print ("\tRecette du crépes")

        print ()

        inv=int(input("\tRecette 3 > Pour combien de personnes ?"))

        print ()

        print ("\tRecette 3 > Pour" ,inv ,"personne, il vous faudra :")

        print ()

        print ("\t-" ,4/4*inv ,"oeufs")

        print ("\t-" ,1/4*inv ,"pincée de sel")

        print ("\t-",0.5/4*inv ,"litres de lait")

        print ("\t-",250/4*inv ,"grammes de farine")

        print ("\t-",2/4*inv ,"cuilliére a soupe de sucre")

        print ("\t-",50/4*inv ,"grammes de beurre")

        print ()

        print ("\tRecette 3 > le temps de préparation sera de 60 minutes")

        print ()

        print ("\tRecette 3 > Bonnne appétit à vous !!")

        print ()

    else: # recette inconnue
        
        print()

        print("\tRecette > Je ne connais pas cette recette")

        print()

    # retourné ou non a la tables des matiéres

    print("\tVoulez vous Revenir a la tables des matiéres ? (o/n)")

    print ()
        
    choice = input("\tRecette > ")

    if choice == 'o':

        main()
            
    elif choice == 'n':

        print ()

        print("\tAu Revoir et à Bientôt !!")

        print ()
    
main() # fin de la def main


