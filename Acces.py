from Client import Client
from Parking import Parking
from Camera import Camera
from Borne_Ticket import Borne_Ticket
from Teleporteur import Teleporteur
from Panneau_Affichage import Panneau_Affichage

class Acces:
	
	def __init__(self, Panneau_Affichage, teleporteur1, teleporteur2, Borne_Ticket, Camera):
		self.panneau_affichage = Panneau_Affichage
		self.teleporteur1 = teleporteur1
		self.teleporteur2 = teleporteur2
		self.borne_bicket = Borne_Ticket
		self.camera = Camera
		
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
