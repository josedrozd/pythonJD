palabra = input("Escriba la palabra a determinar que letras aparecen un numero primo de veces: ")

letras = []

for L in palabra:
	cant=0
	ok=True
	for tupla in letras:
		if L.lower() == tupla[0]:
			ok=False	
	if ok:
		for i in range(len(palabra)):
			if (L.lower() == palabra[i].lower()):
				cant += 1
		letras.append((L.lower(), cant))

primas = []

for tupla in letras:
	if tupla[1] > 1:
		print("La letra ",tupla[0]," aparece: ",tupla[1]," veces")
	else: 
		print("La letra ",tupla[0]," aparece: ",tupla[1]," vez")
	if (tupla[1] in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)):  #En esta linea escribi los primeros numeros primos suponiendo que el string no iba a contener tantos caracteres, porque no se me ocurrio otra manera de hacerlo. 
		primas.append(tupla[0])

print ("Las letras que aparecen un numero primo de veces son:", *primas)
