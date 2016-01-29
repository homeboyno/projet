class Teleporteur:
	def __init__(self, tel):
		self.tel = tel
		
	def teleporterVoiture(self, voiture, place):
		placement = Placement()
		voiture.addPlacementV(placement)
		place.addPlacementP(placement)
		
	def teleporterVoitureSuperAbonne(self, voiture):
		return "Votre voiture est bien prise en charge. Bonne journée !"
