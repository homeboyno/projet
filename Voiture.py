from Placement import Placement

class Voiture:
	def __init__(self, hauteur, longueur, immatriculation):
		self.__hauteur = hauteur
		self.__longueur = longueur
		self.__immatriculation = immatriculation
		self.estDansParking = False
		
	@property	
	def hauteur(self): return self.__hauteur
	
	@property
	def longueur(self): return self.__longueur
	
	@property
	def immatriculation(self): return self.__immatriculation

	def addPlacementV(self, Placement):
		self.placement = Placement
		
