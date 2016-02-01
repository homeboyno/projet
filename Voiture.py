from Placement import Placement

class Voiture:
	def __init__(self, hauteur, longueur, immatriculation):
		self.__hauteur = hauteur
		self.__longueur = longueur
		self.__immatriculation = immatriculation
		self.estDansParking = False
		
	@property	
	def hauteur(self): return self.__hauteur
	
	@hauteur.setter
	def hauteur(self, hauteur):
		self.__hauteur = hauteur
	
	@property
	def longueur(self): return self.__longueur
	
	@longueur.setter
	def longueur(self, longueur):
		self.__longueur = longueur
	
	@property
	def immatriculation(self): return self.__immatriculation

	@immatriculation.setter
	def immatriculation(self, immatriculation):
		self.immatriculation = immatriculation
		
	def addPlacementV(self, Placement):
		self.placement = Placement
		
