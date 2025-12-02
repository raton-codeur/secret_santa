from reportlab.pdfgen import canvas

# on veut écrire la correspondance participants (l) <-> code (l_chiffré) dans un pdf

def write_pdf(l, l_chiffré) :
	c = canvas.Canvas("chiffrement.pdf")
	c.setPageSize((595.27, 841.89)) # taille : format A4
	c.setFont("Helvetica", 16)
	width, height = c._pagesize

	message = [
		"Chiffrement des prénoms",
		"(voir page suivante)"
	]

	x = width / 2
	y = height - 100
	for ligne in message :
		c.drawCentredString(x, y, ligne)
		y -= 30

	c.showPage() # page suivante.
	c.setFont("Helvetica", 16)

	y = height - 100
	for i, j in zip(l, l_chiffré) :
		c.drawCentredString(x, y, f"{i} = {j}")
		y -= 30

	c.save()
