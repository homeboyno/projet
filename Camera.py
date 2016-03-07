'''from Voiture import Voiture'''
import random
import string

class Camera:
	
	def __init__(self):
		pass
		
	def capturerHauteur(self, Voiture):
		#Voiture.hauteur = (random.randint(140,255))   #Voiture.hauteur
		return random.randint(140,255)
				
	def capturerLongueur(self, Voiture):
		#Voiture.longueur = (random.randint(290,475))#Voiture.longueur
		return random.randint(290,475)
		
	def capturerImmatr(self, Voiture):
		#string.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		#Voiture.immatriculation = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(random.randint(0,9)) + str(random.randint(0,9)) #Voiture.immatriculation
		return str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(random.randint(0,9)) + str(random.randint(0,9))

# rappel des places de parking : (randint(300,450)) ,True, (randint(150,250)))
