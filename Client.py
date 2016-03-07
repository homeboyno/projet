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
		"""
		add a subscription for this client
		"""
		self.__estAbonne = True
		self.abonnement = Abonnement
		
	def nouvelle_voiture(self, hautV, longV, imma):
		"""
		replace the client car by his actual car
		"""
		self.voiture = Voiture(hautV, longV, imma)
		
	def seDesabonner(self):
		"""
		Delete the subscription
		"""
		self.estAbonne = False
		#del self.abonnement    Conserver qu'il a ete abonner pour faire des stats.

	def demanderMaintenance(self):
		maintenance = raw_input("Voulez vous une maintenance ? 1:True 2:False ")
		while True:
			if maintenance == '1':
				return True
			elif maintenance == '2':
				return False
			else:
				maintenance = raw_input("Voulez vous une maintenance ? 1:True 2:False ")
		
	def demanderLivraison(self):
		livraison = raw_input("Voulez vous une livraison ? 1:True 2:False ")
		while True:
			if livraison == '1':
				return True
			elif livraison == '2':
				return False
			else:
				livraison = raw_input("Voulez vous une livraison ? 1:True 2:False ")
		
	def demanderEntretien(self):
		entretien = raw_input("Voulez vous un entretien ? 1:True 2:False ")
		while True:
			if entretien == '1':
				return True
			elif entretien == '2':
				return False
			else:
				entretien = raw_input("Voulez vous un entretien ? 1:True 2:False ")
		
	def entrerParking(self, Acces):
		"""
		Scan the car of the client 
		"""
		Acces.lancerProcedureEntree(self)
		self.nbFrequentations += 1
		self.voiture.estDansParking = True
		
		
