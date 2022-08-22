import hangman, reversegam, tictactoeModificado, json, os.path
import PySimpleGUI as sg

def registrar(nombre,juego):

	archivo = open("registro.txt","r")
	rec = json.load(archivo)

	ok=False
	i=0
	for j in rec:
		if(j["nombre"]==nombre):
			ok=True
			break
		i+=1

	if(not ok):
		j={"nombre":nombre,"jugados":[juego]}
		rec.append(j)
	else:
		j["jugados"].append(juego)
		rec[i]=j

	archivo= open("registro.txt","w")

	json.dump(rec,archivo)

	archivo.close()


def main(args):

	if (not os.path.isfile("registro.txt")):
		archivo=open("registro.txt", "w")
		j=[]
		json.dump(j,archivo)
		archivo.close()

	sg.theme('DarkAmber')
	layout = [[sg.Text("Escriba su nombre "),sg.InputText("")],[sg.Text("Elegi a que queres jugar: "),sg.Combo(["Ahorcado","Ta-Te-Ti","Otello"])],[sg.Ok(),sg.Button("Salir")]]
	window = sg.Window('Juegos en Python', layout)
	
	while True:
		evento, valores = window.read()
		if evento == "Salir":
			break
		else:
			if (evento=="Ok") and (valores[0] != "") and (valores[1]!=""):
				nombre=valores[0]
				window.Hide()
				if valores[1]=="Ahorcado":
					hangman.main()
					registrar(nombre,"Ahorcado")
				elif valores[1]=="Ta-Te-Ti":
					tictactoeModificado.main()
					registrar(nombre,"Ta-TE-TI")
				else:
					reversegam.main()
					registrar(nombre,"Otello")
				break
			else:
				if (valores[0] == ""):
					sg.popup("Olvido el nombre!")
				else:
					sg.popup("Elija un juego!")
				

	window.Close()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

