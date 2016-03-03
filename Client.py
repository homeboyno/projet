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
		maintenance = input("Voulez vous une maintenance ? True/False ")
		maintenance = bool(maintenance)
		return maintenance
		
	def demanderLivraison(self):
		''', dateLiv, heure, adresseLiv'''
		livraison = input("Voulez vous une livraison ? True/False ")
		livraison = bool(livraison)
		return livraison
		
	def demanderEntretien(self):
		entretien = input("Voulez vous un entretien ? True/False ")
		entretien = bool(entretien)
		return entretien
		
	def entrerParking(self, Acces):
		Acces.lancerProcedureEntree(self)
		self.nbFrequentations += 1
		self.voiture.estDansParking = True
		
		
