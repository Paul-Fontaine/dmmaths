# dmmaths

## fonctions distance
- [ ] distance euclidienne : sqrt(x² + y²)
- [ ] distance 1 : Δx + Δy
- [ ] distance infinie : max(Δx, Δy)
- [ ] écart de Ward : (p1p2 / p1+p2)  *  distance_euclidienne(g1, g2)²
		écart entre 2 classes de poids p et de centre de gravité g
- [ ] distance minimale : retourne les deux points les plus proches d'un ensemble de points

## regroupement en classe
*question 4*
- [ ] regrouper les deux points les plus proches en une classe Γ<sub>1</sub> en utilisant la fonction distance minimale
- [ ] trouver le point le plus proche de la classe Γ<sub>1</sub> en utilisant la fonction distance minimale avec g<sub>1</sub> le centre de gravité de la classe Γ<sub>1</sub>
- [ ] ajouter le point trouvé à la classe Γ<sub>1</sub> pour créer la classe Γ<sub>2</sub>

*question 5*
- [ ] répeter l'opération pour tous les points restants

*question 6, 7*
- [ ] se documenter sur les dendrogrammes
- [ ] construire le dendrogramme au fur et à mesure du regroupement, ajouter un bout de code à la *question 5*

## étape finale
- [ ] reprendre toutes les questions précédentes pour créer le dendrogramme du tableau de 29 points dans un espace de dimension 9
- [ ] adapter les fonctions de distance pour 9 dimensions
