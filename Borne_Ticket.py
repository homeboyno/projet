'''from Client import Client
from Parking import Parking'''

class Borne_Ticket:
	def __init__(self):
		pass
		
	def delivrerTicket(self, Client):
		#Client.ticket =  
		return "Voici votre ticket : Ticket"
		
	def proposerServices(self):
		pass
		
	def proposerAbonnements(self, Client, Parking):
		pass
	
	def recupererInfosCarte(self, Client):
		return Client.nom;
		
	def proposerTypePaiement():
		return "Quel est le mode de paiement que vous avez choisis ?"
		
	def add(self, acces):
		self.acces = acces
