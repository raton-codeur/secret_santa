l = ["Michel", "Monique", "Aurore", "Thomas", "Florian", "Charlotte", "Fred", "Maud", "Line", "Quentin"] # la liste des participants.

# on veut associer chaque participant de l à un autre participant, à qui il devra offrir un cadeau de Nöel.
# si possible, personne ne doit savoir qui lui offre son cadeau.

import random
random.shuffle(l)

# on veut chiffrer l pour que les participants ne soient pas facilement lisibles.
# on associe un code aléatoire à chaque participant.

l_chiffré = ["".join([chr(random.randint(ord('A'), ord('Z'))) for i in range(6)]) for i in l]

# on veut écrire la correspondance participant <-> code dans un fichier pdf.

from reportlab.pdfgen import canvas

canvas = canvas.Canvas("chiffrement.pdf")
canvas.setPageSize((595.27, 841.89)) # taille : format A4
canvas.setFont("Helvetica", 16)
width, height = canvas._pagesize

message = [
    "Chiffrement des prénoms",
    "(voir page suivante)"
]

x = width / 2
y = height - 100
for ligne in message :
	canvas.drawCentredString(x, y, ligne)
	y -= 30

canvas.showPage() # page suivante.
canvas.setFont("Helvetica", 16)

y = height - 100
for i, j in zip(l, l_chiffré) :
	canvas.drawCentredString(x, y, f"{i} = {j}")
	y -= 30

canvas.save()

# fin de la partie pdf.

pas_possible = [("Maud", "Line"), ("Monique", "Michel"), ("Aurore", "Thomas"), ("Charlotte", "Fred")] # la liste des associations qu'on ne veut pas.

# s : un prénom chiffré
# renvoie le prénom déchiffré
def déchiffre(s) :
	for i in range(len(l)) :
		if l_chiffré[i] == s :
			return (l[i])

# début de construction de l chiffré et mélangé.

l_chiffré_mélangé = l_chiffré.copy()
recommencer = True
while recommencer :
	random.shuffle(l_chiffré_mélangé)
	recommencer = False
	for i in range(len(l)) :
		if l_chiffré_mélangé[i] == l_chiffré[i] : # un participant ne doit pas être associé à lui même.
			recommencer = True
		for j in pas_possible :
			if l[i] in j and déchiffre(l_chiffré_mélangé[i]) in j :
				recommencer = True

# fin de construction de l chiffré et mélangé.

# l_chiffré_mélangé_déchiffré = [déchiffre(i) for i in l_chiffré_mélangé]
# print(l, l_chiffré, l_chiffré_mélangé, l_chiffré_mélangé_déchiffré, sep = "\n\n", end = "\n\n")

for i in range(len(l)) :
	if (l[i] == "Quentin") :
		print("pour Quentin : " + déchiffre(l_chiffré_mélangé[i]))
	else :
		print(f"pour {l[i]} : {l_chiffré_mélangé[i]}")
