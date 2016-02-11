'''from Voiture import Voiture
from Place import Place'''

class Teleporteur:
	def __init__(self, tel):
		self.tel = tel  #telEntree ou telSortie.
		
	def teleporterVoiture(self, voiture, place):
		placement = Placement(voiture, place) #Creer un nouveau placement entre la voiture et la place
		voiture.addPlacementV(placement)
		place.addPlacementP(placement)
		return "Votre voiture est bien prise en charge. Bonne journee !"
		
	def teleporterVoitureSuperAbonne(self, voiture):
		if(Parking.recherchePlace(voiture) == nul):
			return "Votre voiture est bien prise en charge. Bonne journee !"
		else:
			teleporterVoiture(voiture, Parking.recherchePlace(voiture))
		
		
#place = Recuperer une place existante avec Parking.rechercherPlace.
#placement = Placement(voiture, place)
#voiture.addPlacementV(placement)
