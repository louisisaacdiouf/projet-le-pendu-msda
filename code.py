# --------------------------------------------------------------------
# DEBUT DU PROGRAMME
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# CHOIX DU NIVEAU DE JEU 
# --------------------------------------------------------------------
def niveau():
	level = int(input("Choississez le niveau de jeu...   1 ou 2 ou 3 \n"))
	
	while (level != 1 and level != 2 and level != 3):
		level = int(input("Veuillez choisir un niveau entre 1, 2 et 3 \n"))

	return level
		
# --------------------------------------------------------------------
# IMPORTATION DES MOTS
# --------------------------------------------------------------------
def importerMots(level):
	if (level == 1):
		fichier = open("1-5_Mots.txt","r")
	if (level == 2):
		fichier = open("6-8_Mots.txt","r")
	if (level == 3):
		fichier = open("10-Plus_Mots.txt","r")

	s=fichier.readline()
	mots=s.split()
	print(str(len(mots))+" mots chargés pour le niveau "+str(level)+". \n")
	return mots

# --------------------------------------------------------------------
# CHOIX DU MOT A DEVINER
# --------------------------------------------------------------------
def choix_mot_a_deviner(mots):
	import random
	mot_hasard_index = random.randint(1,len(mots))
	mot_hasard = mots[mot_hasard_index]

	print("Vous devrez deviner un mot de "+str(len(mot_hasard))+" lettres. A vous de jouer !! \n")

	variablesGlobales = globals()
	variablesGlobales["champ"] = ""
	
	for x in range(1,len(mot_hasard)+1):
		variablesGlobales["champ"] += "_"

	variablesGlobales["mot_depart"] = mot_hasard

	return mot_hasard

# --------------------------------------------------------------------
# PROPOSITION D'UNE LETTRE PAR L'UTILISATEUR
# --------------------------------------------------------------------
def deviner_lettre(mot):
	variablesGlobales = globals()

	vu = variablesGlobales["mot_depart"]
	

	lettre = input("Quelle lettre pensez-vous qu'il y a dans le mot mystère ? \n")

	while (len(lettre) != 1):
		if (len(lettre)==0):
			print("Veuillez entrer un caractère svp")
		else:
			print("Veuillez entrer un seul caractère svp")
			lettre = input("Quelle lettre pensez-vous qu'il y a dans le mot mystère ? \n")

	lettre = lettre.upper()
	presence = mot.count(lettre)

	if (presence > 0):
		print("VRAI !! Vous avez deviné une lettre du mot mystère \n")
		mot = mot.replace(lettre,"",1)
		tentatives("up")
		x = vu.find(lettre)
		j = 0

		text = list(variablesGlobales["champ"])
		while (text[x] == lettre):
			x = [i for i, n in enumerate(vu) if n == lettre][j]
			j+=1

		text[x] = lettre
		
		variablesGlobales["champ"] = "".join(text)

	else:
		print("FAUX")
		tentatives("down")

	print(variablesGlobales["champ"])

	return mot
		
# --------------------------------------------------------------------
# EXECUTION DES ESSAIS DU JEU
# --------------------------------------------------------------------
def essais(mot):
	restant_mot = mot
	variablesGlobales = globals()
	while (len(restant_mot)>0 and ((variablesGlobales["tentatives_restantes"]!=0) and (variablesGlobales["points_erreurs"]!=0))):
		restant_mot = deviner_lettre(restant_mot)
		print("Lettres restant à deviner : "+str(len(restant_mot))+" \n")
	
	if (len(restant_mot) == 0):
		print("FELICITATIONS !!! VOUS AVEZ GAGNE LA PARTIE !!! \n")
		print("LE MOT A DEVINER ETAIT "+mot+" !! BIEN JOUE !! \n")
	else:
		print("DOMMAGE !!! VOUS ETES PENDU !!! \n")
		print("LE MOT A DEVINER ETAIT "+mot+" !! \n")

# --------------------------------------------------------------------
# GESTION DES TENTATIVES ET DES POINTS-ERREURS
# --------------------------------------------------------------------
def tentatives(etat):
	variablesGlobales = globals()
	if (etat=="up"):
		variablesGlobales["tentatives_restantes"] += 1
		variablesGlobales["points_erreurs"] = 3
		print("Vous avez trouvé une lettre !! Vous gagnez une tentative !! \n")
	if (etat=="down"):
		if (variablesGlobales["points_erreurs"] > 1):
			variablesGlobales["points_erreurs"] -= 1
			print("Cette lettre n'est pas dans le mot. Vous perdez un point erreur. \n")
		else:
			if (variablesGlobales["tentatives_restantes"] > 0):
				variablesGlobales["tentatives_restantes"] -= 1
				variablesGlobales["points_erreurs"] = 3
				print("Vous avez faussé 3 fois. Vous perdez une tentative.\n")
			else:
				variablesGlobales["tentatives_restantes"] = 0
				variablesGlobales["points_erreurs"] = 0
	
	print("Nombre de tentatives restantes : "+str(tentatives_restantes)+" \n")
	print("Nombre de points erreurs restants : "+str(points_erreurs)+" \n")

# --------------------------------------------------------------------
# BLOC PRINCIPAL
# --------------------------------------------------------------------
def execution():
	global champ
	global tentatives_restantes
	global points_erreurs
	global mot_depart

	tentatives_restantes = 6
	points_erreurs = 3

	niv = niveau()
	words = importerMots(niv)
	mot_mystere = choix_mot_a_deviner(words)
	lettres_restant_a_deviner = mot_mystere

	essais(lettres_restant_a_deviner)



# --------------------------------------------------------------------
# Exécution du BLOC PRINCIPAL
# --------------------------------------------------------------------
execution()

# --------------------------------------------------------------------
# FIN DU PROGRAMME
# --------------------------------------------------------------------