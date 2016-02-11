#from Placement import Placement

class Place:
	def __init__(self, numero, niveau, longueur, estLibre, hauteur):
		self.numero = numero
		self.__niveau = niveau
		self.__longueur = longueur
		self.__estLibre = estLibre
		self.__hauteur = hauteur
		self.idPlace = str(niveau) + str(numero)
		
	@property
	def niveau(self):return self.__niveau
	
	@property
	def longueur(self):return self.__longueur
	
	@property
	def estLibre(self):return self.__estLibre
	
	@property
	def hauteur(self):return self.__hauteur
	
	def addPlacementP(self, Placement):
		self.placement = Placement
