
class Parking:
	def __init__(self, nbPlacesParNiveau, prix, nbNiveau):
		self.__nbPlacesParNiveau = nbPlacesParNiveau
		self.__prix = prix
		self.nbNiveau = nbNiveau
		self.places = []
		self.nbPlacesLibres = nbPlacesParNiveau*nbNiveau
		self.abonnement = []
		
	def recherchePlace(self, voiture):
		"""
		seach for each places if the car can get in		
		return a specific value "None" in case no place are free for the car
		"""
		for pla in self.places:
			if(pla.estLibre and (pla.longueur >= voiture.longueur) and (pla.hauteur >= voiture.hauteur)):
				self.nbPlacesLibres -= 1
				return pla
		print("Votre voiture est trop grande pour les places disponible actuellement.")
		return None
		
	def NbPlacesLibreAuNiveau(self, Niveau):
		rst = 0
		for pla in self.places:
			if ((str(pla.niveau) == str(Niveau)) and pla.estLibre ):
				rst = rst +1
		return rst
		
	def addAbonnement(self, abonnement):
		self.abonnement.append(abonnement)
		
	@property
	def nbPlacesParNiveau(self): return self.__nbPlacesParNiveau
		
	@property
	def prix(self): return self.__prix
