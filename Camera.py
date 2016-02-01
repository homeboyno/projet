from Voiture import Voiture
from random import randint

class Camera:
	
	def __init__(self):
		pass
		#self.aaaaaaaaaa = None ?
		
	def capturerHauteur(self, Voiture):
		Voiture.hauteur = (randint(100,200))#Voiture.hauteur
		
	def capturerLongueur(self, Voiture):
		Voiture.longueur = (randint(250,400))#Voiture.longueur
		
	def capturerImmatr(self, Voiture):
		string.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		Voiture.immatriculation = str(randint(0,999) + random.choice(string.letters) + random.choice(string.letters) + randint(0,999)) #Voiture.immatriculation
		
	def add(acces):
		self.acces = acces
