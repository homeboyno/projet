'''from Voiture import Voiture'''
import random
import string

class Camera:
	
	def __init__(self):
		pass
		
	def capturerHauteur(self, Voiture):
		#Voiture.hauteur = (random.randint(100,200))   #Voiture.hauteur
		return random.randint(100,200)
				
	def capturerLongueur(self, Voiture):
		#Voiture.longueur = (random.randint(250,400))#Voiture.longueur
		return random.randint(250,400)
		
	def capturerImmatr(self, Voiture):
		#string.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		#Voiture.immatriculation = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(random.randint(0,9)) + str(random.randint(0,9)) #Voiture.immatriculation
		return str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(random.randint(0,9)) + str(random.randint(0,9))
