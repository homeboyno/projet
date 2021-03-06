#!/usr/bin/python
# -*-coding:UTF-8 -*-

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

def demandeEntree():
	possede_card = raw_input("Avez vous une carte ? 1:True 2:False ")
	possede_carte = stringToBool(possede_card)
	if possede_carte:
		print("Les cartes abonnement ne sont pas prisent en charge.")
		return
		#clt = input(BorneTicket.recupererInfosCarte(carte))
	else:	
		nom = raw_input("Quel est votre nom ? ")
		adresse = raw_input("Quel est votre adresse ? ")
		clt = Client(nom, adresse)
	
	if not(clt.estAbonne or clt.estSuperAbonne):
		clt.entrerParking(acces1)
		place = parking.recherchePlace(clt.voiture)
		if place != None:
			BorneTicket.proposerServices(clt, parking)
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
		if n == '1':
			return True
		elif n == '2':
			return False
		else:
			n = raw_input("1:True 2:False ")
	
if __name__ == '__main__':
	recuperation = raw_input("Voulez vous recuperer les anciennes donnees ? 1:True 2:False ")
	recup = stringToBool(recuperation)
	if recup:
		fichier = open('parking.saved', 'r')
		p = pickle.Unpickler(fichier)  
		parking = p.load() 
		fichier.close()
		
		fichier = open('cam1.saved', 'r')
		p = pickle.Unpickler(fichier)  
		cam1 = p.load() 
		fichier.close()
		
		fichier = open('pano.saved', 'r')
		p = pickle.Unpickler(fichier)  
		pano = p.load() 
		fichier.close()
		
		fichier = open('telEntre.saved', 'r')
		p = pickle.Unpickler(fichier)  
		telEntre = p.load() 
		fichier.close()
		
		fichier = open('telSortie.saved', 'r')
		p = pickle.Unpickler(fichier)  
		telSortie = p.load() 
		fichier.close()
		
		fichier = open('BorneTicket.saved', 'r')
		p = pickle.Unpickler(fichier)  
		BorneTicket = p.load() 
		fichier.close()
		
		fichier = open('acces1.saved', 'r')
		p = pickle.Unpickler(fichier)  
		acces1 = p.load() 
		fichier.close()
		
		
		print("Recuperation des donnees terminer")
	else:
		with open('TracePassage.txt', 'w') as fichier:
			fichier.write("Création du parking\n\nListe des places :\n")
		parking = Parking(10,5,4)
		#Creation des places de parking
		for etage in range (0,parking.nbNiveau): 
			string.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
			etage_lettre = string.letters[etage]
			for numero in range (1,parking.nbPlacesParNiveau +1):
				pla = Place(numero, etage_lettre, (randint(300,450)) ,True, (randint(150,250)))
				parking.places.append(pla)
				print("Place : " + str(pla.idPlace) + ". Longueur : " + str(pla.longueur) + ". Hauteur " + str(pla.hauteur))
				with open('TracePassage.txt', 'a') as fichier:
					fichier.write("Place : " + str(pla.idPlace) + ". Longueur : " + str(pla.longueur) + ". Hauteur " + str(pla.hauteur) + "\n")
		cam1 = Camera()
		pano = Panneau_Affichage()
		telEntre = Teleporteur("telEntre")
		telSortie = Teleporteur("telSortie")
		BorneTicket = Borne_Ticket()
		acces1 = Acces(pano, telEntre, telSortie, BorneTicket, cam1, parking)
		

	continuer = True
	while continuer:
		select = raw_input("Selectionner une option :\n\t1: Demande entree\n\t2: Demande sortie\n\t3: Aides\n")
		if select == '1':
			demandeEntree()
		elif select == '2':
			placeID = raw_input("Quel place occupe votre vehicule ? ")
			demandeSortie(placeID, parking, telSortie)
		elif select == '3':
			aide()
		else:
			continue
			
		print(pano.afficherNbPlacesDisponible(parking))
		continuee = raw_input("Continuer le programme ? 1:True 2:False ")
		continuer = stringToBool(continuee)
		
		if continuer == False:
			saves = raw_input("Voulez vous sauvegarder les donnees ? 1:True 2:False ")
			save = stringToBool(saves)
			if save:
				output = open('parking.saved', 'w')
				pickle.dump(parking, output)
				output.close()
				
				output = open('cam1.saved', 'w')
				pickle.dump(cam1, output)
				output.close()
				
				output = open('pano.saved', 'w')
				pickle.dump(pano, output)
				output.close()
				
				output = open('telEntre.saved', 'w')
				pickle.dump(telEntre, output)
				output.close()
				
				output = open('telSortie.saved', 'w')
				pickle.dump(telSortie, output)
				output.close()
				
				output = open('BorneTicket.saved', 'w')
				pickle.dump(BorneTicket, output)
				output.close()
				
				output = open('acces1.saved', 'w')
				pickle.dump(acces1, output)
				output.close()
	print("Fin du programme")
	
