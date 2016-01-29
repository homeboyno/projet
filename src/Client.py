from Abonnement import Abonnement
from Acces import Acces

class Client:
	
	def __init__(self, nom, adresse):
		self.nom = nom
		self.adresse = adresse
		self.estAbonne = False
		self.estSuperAbonne = False
		self.nbFrequentations = 0
				
	def sAbonner(self, Abonnement):
		self.__estAbonne = True
		self.abonnement = Abonnement
		
	def nouvelle_voiture(self, hautV, longV, imma):
		self.voiture = Voiture(hautV, longV, imma)
		
	def seDesabonner(self):
		self.estAbonne = False
		del self.abonnement

	def demanderMaintenance(self):
		pass
		
	def demanderLivraison(self, dateLiv, heure, adresseLiv):
		pass
		
	def demanderEntretien(self):
		pass
		
	def entrerParking(self, Acces):
		self.nbFrequentations += 1
		self.voiture.estDansParking = True
		Acces.lancerProcedureEntree
