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
from Abonnement import Abonnement
from random import randint
import string
import pickle 
'''panneau_affi1 = Panneau_Affichage()
tel_entree = Teleporteur(TelEntree)
tel_sortie = Teleporteur(TelSortie)
borne_ticket = Borne_Ticket()
camera1 = Camera()
acces1 = Acces(panneau_affi, tel_entree, tel_sortie, borne_ticket, camera1, parking)
borne_ticket.add(acces1)
camera1.add(acces1)'''

def demandeEntree():
	possede_card = input("Avez vous une carte ? 1:True 2:False ")
	possede_carte = stringToBool(possede_card)
	if possede_carte:
		print("Les cartes abonnement ne sont pas prisent en charge.")
		return
		#clt = input(BorneTicket.recupererInfosCarte(carte))
	else:	
		nom = input("Quel est votre nom ? ")
		adresse = input("Quel est votre adresse ? ")
		clt = Client(nom, adresse)
	
	if not(clt.estAbonne or clt.estSuperAbonne):
		place = parking.recherchePlace(clt.voiture)
		if place != None:
			BorneTicket.proposerServices(clt, parking)
			clt.entrerParking(acces1)
			telEntre.teleporterVoiture(clt.voiture, place)
		else:
			print("Aucune place disponible pour votre véhicule.")
	else:
		clt.entrerParking(acces1)
		print(telEntre.teleporterVoitureSuperAbonne())
		
		
def demandeSortie(placeID, parking, telSortie):
	telSortie.retirerVoiture(placeID, parking)

def aide():
	print(pano.afficherNbPlacesDisponible(parking))

def stringToBool(n):
	while True:
		if n == 1:
			return True
		elif n == 2:
			return False
		else:
			n = input("1:True 2:False ")


	
if __name__ == '__main__':
	recuperation = input("Voulez vous recuperer les anciennes donnees ? 1:True 2:False ")
	recup = stringToBool(recuperation)
	if recup:
		print("recup" + recup)
		input = open('parking.saved', 'r')
		p = pickle.Unpickler(input)  
		parking = p.load() 
		input.close()
		print("Recuperation des donnees terminer")
	else:
		parking = Parking(10,5,4)
		#Creation des places de parking
		for etage in range (0,parking.nbNiveau): 
			string.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
			etage_lettre = string.letters[etage]
			for numero in range (1,parking.nbPlacesParNiveau +1):
				pla = Place(numero, etage_lettre, (randint(300,450)) ,True, (randint(150,250)))
				parking.places.append(pla)
				print("Place : " + str(pla.idPlace) + ". Longueur : " + str(pla.longueur) + ". Hauteur " + str(pla.hauteur))
		
		cam1 = Camera()
		pano = Panneau_Affichage()
		telEntre = Teleporteur("telEntre")
		telSortie = Teleporteur("telSortie")
		BorneTicket = Borne_Ticket()
		acces1 = Acces(pano, telEntre, telSortie, BorneTicket, cam1, parking)


	continuer = True
	while continuer:
		select = input("Selectionner une option :\n\t1: Demande entree\n\t2: Demande sortie\n\t3: Aides\n")
		if select == 1:
			demandeEntree()
		elif select == 2:
			placeID = input("Quel place occupe votre vehicule ? ")
			demandeSortie(placeID, parking, telSortie)
		elif select == 3:
			aide()
		else:
			continue
			
		print(pano.afficherNbPlacesDisponible(parking))
		continuee = input("Continuer le programme ? 1:True 2:False ")
		continuer = stringToBool(continuee)
		
		if continuer == False:
			saves = input("Voulez vous sauvegarder les donnees ? 1:True 2:False ")
			save = stringToBool(saves)
			if save:
				output = open('parking.saved', 'w')
				pickle.dump(parking, output)
				output.close()
	print("Fin du programme")
	
	
	
	#clt.nouvelle_voiture()
	'''vtr = Voiture(150,50,"F4SD5")
	print(vtr.hauteur)
	print(vtr.longueur)
	print(vtr.immatriculation)'''
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


		
'''	clt = Client("Robert", "rue de la foret")
	
	if not(clt.estAbonne or clt.estSuperAbonne):
		place = parking.recherchePlace(clt.voiture)
		if place != None:
			BorneTicket.proposerServices(clt, parking)
			clt.entrerParking(acces1)
			telEntre.teleporterVoiture(clt.voiture, place)
		else:
			print("Aucune place disponible pour votre véhicule.")
	else:
		clt.entrerParking(acces1)
		print(telEntre.teleporterVoitureSuperAbonne())
'''
	
