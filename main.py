#!/usr/bin/python
# -*-coding:UTF-8 -*-

# Classe faites : Camera ; Panneau_affichage; Acces; Teleporteur; Place; 
# Classe à completer : 
# Classe à faire : 
#
#
#
from Client import Client
from Parking import Parking
from Camera import Camera
from Borne_Ticket import Borne_Ticket
from Teleporteur import Teleporteur
from Panneau_Affichage import Panneau_Affichage
from Voiture import Voiture
from Panneau_Affichage import Panneau_Affichage
from Place import Place
from Acces import Acces
from random import randint
import string
'''panneau_affi1 = Panneau_Affichage()
tel_entree = Teleporteur(TelEntree)
tel_sortie = Teleporteur(TelSortie)
borne_ticket = Borne_Ticket()
camera1 = Camera()
acces1 = Acces(panneau_affi, tel_entree, tel_sortie, borne_ticket, camera1, parking)
borne_ticket.add(acces1)
camera1.add(acces1)'''



if __name__ == '__main__':
#Parking, places, 
	parking = Parking(10,5,4)
	
	#Creation des places de parking
	for etage in range (0,parking.nbNiveau): #0Correspond au RDC, et 2 au dernier étage.
		string.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		etage_lettre = string.letters[etage]
		for numero in range (1,parking.nbPlacesParNiveau +1):
			pla = Place(numero, etage_lettre, (randint(300,450)) ,True, (randint(150,250)))
			parking.places.append(pla)
			print("Place : " + str(pla.idPlace) + ". Longueur : " + str(pla.longueur) + ". Hauteur " + str(pla.hauteur))
	
	cam1 = Camera()
	pano = Panneau_Affichage()
	acces1 = Acces(pano,"a","a","a",cam1 ,parking)
	
	
	
	clt = Client("Robert", "rue de la foret")
	
	clt.entrerParking(acces1)
	
	
	
	
	#clt.nouvelle_voiture()
	vtr = Voiture(150,50,"F4SD5")
	print(vtr.hauteur)
	print(vtr.longueur)
	print(vtr.immatriculation)
	#park = Parking()
	#pano = Panneau_Affichage(park)
	#pano.afficherNbPlacesDisponible()



'''
Procedure pour initialiser le projet (no verif)
	creer panneau affichage
	creer les deux teleporteurs
	creer camera
	creer acces (avec tout les param precedent
	creer borneTicket
	x2
	creer parking
	creer un emseble de place
'''
