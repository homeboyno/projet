'''from Voiture import Voiture
from Place import Place'''
from Placement import Placement 

class Teleporteur:
	def __init__(self, tel):
		self.tel = tel  #telEntree ou telSortie.
		
	def teleporterVoiture(self, voiture, place):
		placement = Placement(voiture, place) #Creer un nouveau placement entre la voiture et la place
		voiture.addPlacementV(placement)
		place.addPlacementP(placement)
		print("Votre voiture est bien prise en charge. Place: "+ str(place.idPlace) +". Bonne journee !")
		
	def teleporterVoitureSuperAbonne(self, voiture):
		if(Parking.recherchePlace(voiture) == None):
			print("Votre voiture est bien prise en charge. Bonne journee !")
		else:
			teleporterVoiture(voiture, Parking.recherchePlace(voiture))
		
	def retirerVoiture(self, placeID, parking):
		for pla in parking.places:
			if pla.idPlace == placeID and pla.estLibre == False:
				pla.placement.partirPlace()
				parking.nbPlacesLibres += 1 
				print("Veuillez patienter le temps que votre vehicule arrive.")
				break
		print("La place demander est errone")
		
#place = Recuperer une place existante avec Parking.rechercherPlace.
#placement = Placement(voiture, place)
#voiture.addPlacementV(placement)
