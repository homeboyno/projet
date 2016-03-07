'''from Client import Client
from Parking import Parking'''
from Abonnement import Abonnement
class Borne_Ticket:
	def __init__(self):
		pass
		
	def delivrerTicket(self, Client):
		#Client.ticket =  
		return "Voici votre ticket : Ticket"
		
	def proposerServices(self, Client, Parking):
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
		abonnement_ = input("Voulez vous vous abonner ? 1:True 2:False ")
		while True:
			if abonnement_ == 1:
				abo = Abonnement()
				Client.sAbonner(abo)
				Parking.addAbonnement(abo)
				break
			elif abonnement_ == 2:
				break
			else:
				abonnement_ = input("Voulez vous vous abonner ? 1:True 2:False ")
		
			
	
	def recupererInfosCarte(self, Client):
		return Client;
		
	def proposerTypePaiement(self):
		paiement = input("Quel est le mode de paiement que vous avez choisis ?  CB/Espece : ")
		return paiement
		
	def add(self, acces):
		self.acces = acces
