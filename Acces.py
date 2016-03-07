
class Acces:
	
	def __init__(self, Panneau_Affichage, tel_entree, tel_sortie, Borne_Ticket, Camera, Parking):
		"""
		Construct a new Acces item		
		:param Panneau_Affichage: The panneau_affichage of Acces		
		:param tel_entree: The teleporteur to enter the car in parking
		:param tel_sortie: The teleporteur to out the car from parking		
		:param Borne_Ticket: The borne ticket of Acces 		
		:param Camera: The camara of Access
		:param Parking: The parking of Access
		:return: returns nothing
		"""
		self.panneau_affichage = Panneau_Affichage
		self.tel_entree = tel_entree
		self.tel_sortie = tel_sortie
		self.borne_bicket = Borne_Ticket
		self.camera = Camera
		self.parking = Parking
		
	def actionnerCamera(self, Client):
		"""
		Activate the camera of acces in order to set new param for the Client car. 
		:return: updated client car
		"""
		hauteur = self.camera.capturerHauteur(Client.voiture)
		longueur = self.camera.capturerLongueur(Client.voiture)
		imma = self.camera.capturerImmatr(Client.voiture)
		print("Camera : Hauteur " + str(hauteur) + " - Longueur " + str(longueur) + " - Immatricule " + str(imma))
		Client.nouvelle_voiture(hauteur, longueur, imma)
		return Client.voiture
		
	def actionnerPanneau(self):
		"""
		Out the place available for each stage 
		"""
		self.panneau_affichage.afficherNbPlacesDisponible(self.parking)
		
	def lancerProcedureEntree(self, Client):
		"""
		Execute the two functions
		"""
		self.actionnerCamera(Client)
		self.actionnerPanneau()
		#Obtenir identificateur de place

