#from Abonnement import Abonnement
#from Acces import Acces
from Voiture import Voiture

class Client:
	
	def __init__(self, nom, adresse):
		self.nom = nom
		self.adresse = adresse
		self.estAbonne = False
		self.estSuperAbonne = False
		self.nbFrequentations = 0
		self.voiture = Voiture(1, 1, "1")
		
	def sAbonner(self, Abonnement):
		self.__estAbonne = True
		self.abonnement = Abonnement
		
	def nouvelle_voiture(self, hautV, longV, imma):
		self.voiture = Voiture(hautV, longV, imma)
		
	def seDesabonner(self):
		self.estAbonne = False
		#del self.abonnement    Conserver qu'il a ete abonner pour faire des stats.

	def demanderMaintenance(self):
		maintenance = input("Voulez vous une maintenance ? 1:True 2:False ")
		while True:
			if maintenance == 1:
				return True
			elif maintenance == 2:
				return False
			else:
				maintenance = input("Voulez vous une maintenance ? 1:True 2:False ")
		
	def demanderLivraison(self):
		livraison = input("Voulez vous une livraison ? 1:True 2:False ")
		while True:
			if livraison == 1:
				return True
			elif livraison == 2:
				return False
			else:
				livraison = input("Voulez vous une livraison ? 1:True 2:False ")
		
	def demanderEntretien(self):
		entretien = input("Voulez vous un entretien ? 1:True 2:False ")
		while True:
			if entretien == 1:
				return True
			elif entretien == 2:
				return False
			else:
				entretien = input("Voulez vous un entretien ? 1:True 2:False ")
		
	def entrerParking(self, Acces):
		Acces.lancerProcedureEntree(self)
		self.nbFrequentations += 1
		self.voiture.estDansParking = True
		
		
