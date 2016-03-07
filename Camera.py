import random
import string

class Camera:
	
	def __init__(self):
		pass
		
	def capturerHauteur(self, Voiture):
		"""
		Return a random value to simulate the camera
		"""
		#Voiture.hauteur = (random.randint(140,255))   #Voiture.hauteur
		return random.randint(175,225)
				
	def capturerLongueur(self, Voiture):
		"""
		Return a random value to simulate the camera
		"""
		#Voiture.longueur = (random.randint(290,475))#Voiture.longueur
		return random.randint(275,425)
		
	def capturerImmatr(self, Voiture):
		"""
		Return a random value to simulate the camera
		"""
		#string.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		#Voiture.immatriculation = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(random.randint(0,9)) + str(random.randint(0,9)) #Voiture.immatriculation
		return str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(random.randint(0,9)) + str(random.randint(0,9))

