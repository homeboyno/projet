from Voiture import Voiture
from Place import Place

class Teleporteur:
	def __init__(self, tel):
		self.tel = tel  #telEntrée ou telSortie.
		
	def teleporterVoiture(self, voiture, place):
		placement = Placement(voiture, place) #Creer un nouveau placement entre la voiture et la place
		voiture.addPlacementV(placement)
		place.addPlacementP(placement)
		
	def teleporterVoitureSuperAbonne(self, voiture):
		place = #Recuperer une place existante avec Parking.rechercherPlace.
		placement = Placement(voiture, place)
		voiture.addPlacementV(placement)
		return "Votre voiture est bien prise en charge. Bonne journée !"

