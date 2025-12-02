import random
from write_pdf import write_pdf

l = ["Michel", "Monique", "Aurore", "Thomas", "Florian", "Charlotte", "Fred", "Maud", "Line", "Quentin", "Mathis"] # la liste des participants
random.shuffle(l)

# on veut associer chaque participant à un autre participant

# on veut chiffrer l pour que les participants ne soient pas facilement lisibles.
# on associe un code aléatoire de trois lettres à chaque participant.

l_chiffré = ["".join([chr(random.randint(ord('A'), ord('Z'))) for i in range(3)]) for i in l]

# on a l[i] en correspondance avec l_chiffré[i]

write_pdf(l, l_chiffré)

# s : un prénom chiffré
# renvoie le prénom déchiffré
def déchiffre(s) :
	for i in range(len(l)) :
		if l_chiffré[i] == s :
			return (l[i])

pas_possible = [("Maud", "Line"), ("Monique", "Michel"), ("Aurore", "Thomas"), ("Charlotte", "Fred"), ("Quentin", "Mathis")] # la liste des associations qu'on ne veut pas

# on mélange l_chiffré -> l_chiffré_mélangé

# l[i] (≡ l_chiffré[i])
# doit faire un cadeau à
# l_chiffré_mélangé[i] (≡ déchiffre(l_chiffré_mélangé[i]))

l_chiffré_mélangé = l_chiffré.copy()
recommencer = True
while recommencer :
	random.shuffle(l_chiffré_mélangé)
	recommencer = False
	for i in range(len(l)) :
		if l_chiffré[i] == l_chiffré_mélangé[i] : # pour vérifier qu'un participant n'est pas associé à lui même
			recommencer = True
		for j in pas_possible : # on vérifie que l[i] et déchiffre(l_chiffré_mélangé[i]) ne font pas partie d'une association interdite
			if l[i] in j and déchiffre(l_chiffré_mélangé[i]) in j :
				recommencer = True

# fin de construction de l chiffré et mélangé

l_chiffré_mélangé_déchiffré = [déchiffre(i) for i in l_chiffré_mélangé]

# affichage brut
print(l, l_chiffré, l_chiffré_mélangé, l_chiffré_mélangé_déchiffré, sep = "\n\n")

# affichage en clair
# for i in range(len(l)) :
# 	print(f"pour {l[i]} : {déchiffre(l_chiffré_mélangé[i])}")

# affichage chiffré
# for i in range(len(l)) :
# 	if (l[i] == "Quentin") :
# 		print("pour Quentin : " + déchiffre(l_chiffré_mélangé[i]))
# 	else :
# 		print(f"pour {l[i]} : {l_chiffré_mélangé[i]}")
