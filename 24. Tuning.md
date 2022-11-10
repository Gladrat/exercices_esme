# Exercice 24 : Tuning

A partir du code vu en cours :

```python
class Voiture:
    def __init__(self, vitesse_bridage):
        self.couleur = "rouge"
        self.vitesse_max = 225
        self.bridage(vitesse_bridage)

    def bridage(self, vitesse_bridage):
        if (vitesse_bridage < self.vitesse_max):
            self.vitesse_max = vitesse_bridage
        else:
            print(f"Vitesse incohérente, bridage limité à {self.vitesse_max} km/h par le constructeur")

    def __str__(self):
        return f"Une voiture {self.couleur} roulant à {self.vitesse_max} km/h maximum"

    def get_vitesse_max(self):
        return self.vitesse_max

    def set_vitesse_max(self, nouvelle_vitesse):
        self.bridage(nouvelle_vitesse)
        
    def demarrer(self):
        print("Démarrage de la voiture")


ma_voiture = Voiture(200)
ma_voiture.set_vitesse_max(210)
```

## Phase 1

**Attributs**

- Créer un attribut ``vitesse`` (initialisé à ``0``)
  - C'est la vitesse courante du véhicule
- Créer un attribut ``est_demarree`` (initialisé à `False`)

**Méthodes**

- Créer les méthodes `demarrer()` et `arreter()`
- Une voiture démarre uniquement si elle n'est pas déjà démarrée
- Une voiture s'arrête si elle est démarrée et que sa vitesse est à 0

## Phase 2

- Créer la méthode `rouler(vitesse)` qui prend en paramètre une ``vitesse`` cible
- Une voiture ne peut rouler que si elle est démarrée
- ``rouler(vitesse)`` incrémente la vitesse de la voiture depuis sa ``vitesse actuelle`` jusqu'à la ``vitesse cible``, sans jamais dépasser la ``vitesse maximale``

## Phase 3

- Permettre de choisir la couleur de la voiture à sa construction