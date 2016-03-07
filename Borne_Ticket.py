
from Abonnement import Abonnement
class Borne_Ticket:
	def __init__(self):
		"""
		empty constructor
		"""
		pass
		
	def delivrerTicket(self, Client):
		"""
		print the Ticket
		"""
		#Client.ticket =  
		return "Voici votre ticket : Ticket"
		
	def proposerServices(self, Client, Parking):
		"""
		Propose to bought a susbscription
		print the Ticket delivred
		"""
		if Client.estAbonne == True:
			maintenance = Client.demanderMaintenance()
			livraison = Client.demanderLivraison()
			entretien = Client.demanderEntretien()
		else:
			print("Les abonnes beneficie d'avantages et de services.")
			self.proposerAbonnements(Client, Parking)
		self.proposerTypePaiement()
		print(self.delivrerTicket(Client))
		
						
	def proposerAbonnements(self, Client, Parking):
		abonnement_ = raw_input("Voulez vous vous abonner ? 1:True 2:False ")
		while True:
			if abonnement_ == '1':
				abo = Abonnement()
				Client.sAbonner(abo)
				Parking.addAbonnement(abo)
				break
			elif abonnement_ == '2':
				break
			else:
				abonnement_ = raw_input("Voulez vous vous abonner ? 1:True 2:False ")
		
			
	def recupererInfosCarte(self, Client):
		return Client;
		
	def proposerTypePaiement(self):
		paiement = raw_input("Quel est le mode de paiement que vous avez choisis ?  1:CB 2:Espece : ")
		while True:
			if paiement == '1':
				return "CB"
				#traiterPaiementCB()
			elif paiement == '2':
				return "Espece"
				#traiterpaiementEspece()
			else:
				paiement = raw_input("Quel est le mode de paiement que vous avez choisis ?  1:CB 2:Espece : ")
		
	def add(self, acces):
		self.acces = acces
