# Classe faites : Camera ; panneau_affichage; acces;
# Classe à completer : Teleporteur
# Classe à faire : 
#
#
#



from Client import Client
#from Parking import Parking
from Camera import Camera
from Borne_Ticket import Borne_Ticket
from Teleporteur import Teleporteur
from Panneau_Affichage import Panneau_Affichage
from Voiture import Voiture
from Panneau_Affichage import Panneau_Affichage

clt = Client("Robert", "rue de la foret")
#clt.nouvelle_voiture()
vtr = Voiture(150,50,"F4SD5")
print(vtr.hauteur)
print(vtr.longueur)
print(vtr.immatriculation)
#park = Parking()
#pano = Panneau_Affichage(park)
#pano.afficherNbPlacesDisponible()

