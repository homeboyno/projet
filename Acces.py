from Client import Client
from Parking import Parking
from Camera import Camera
from Borne_Ticket import Borne_Ticket
from Teleporteur import Teleporteur
from Panneau_Affichage import Panneau_Affichage

class Acces:
	
	def __init__(self, Panneau_Affichage, tel_entree, tel_sortie, Borne_Ticket, Camera, Parking):
		self.panneau_affichage = Panneau_Affichage
		self.tel_entree = tel_entree
		self.tel_sortie = tel_sortie
		self.borne_bicket = Borne_Ticket
		self.camera = Camera
		self.parking = Parking
		
	def actionnerCamera(self, Client):
		hauteur = camera.hauteur(Client.voiture)
		longueur = camera.longueur(Client.voiture)
		imma = camera.immatriculation(Client.voiture)
		Client.nouvelle_voiture(hauteur, longueur, imma)
		return Client.voiture
		
	def actionnerPanneau(self):
		self.panneau_affichage.afficherNbPlacesDisponible()
		
	def lancerProcedureEntree(self, Client):
		actionnerCamera(self, Client)
		actionnerPanneau(self)
		#Obtenir identificateur de place

