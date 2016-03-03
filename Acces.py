'''from Client import Client
from Parking import Parking
from Camera import Camera
from Borne_Ticket import Borne_Ticket
from Teleporteur import Teleporteur
from Panneau_Affichage import Panneau_Affichage'''

class Acces:
	
	def __init__(self, Panneau_Affichage, tel_entree, tel_sortie, Borne_Ticket, Camera, Parking):
		self.panneau_affichage = Panneau_Affichage
		self.tel_entree = tel_entree
		self.tel_sortie = tel_sortie
		self.borne_bicket = Borne_Ticket
		self.camera = Camera
		self.parking = Parking
		
	def actionnerCamera(self, Client):
		hauteur = self.camera.capturerHauteur(Client.voiture)
		longueur = self.camera.capturerLongueur(Client.voiture)
		imma = self.camera.capturerImmatr(Client.voiture)
		print("Camera : Hauteur " + str(hauteur) + " - Longueur " + str(longueur) + " - Immatricule " + str(imma))
		Client.nouvelle_voiture(hauteur, longueur, imma)
		return Client.voiture
		
	def actionnerPanneau(self):
		self.panneau_affichage.afficherNbPlacesDisponible(self.parking)
		
	def lancerProcedureEntree(self, Client):
		self.actionnerCamera(Client)
		self.actionnerPanneau()
		#Obtenir identificateur de place

