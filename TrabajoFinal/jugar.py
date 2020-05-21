import PySimpleGUI as sg
import ScrabbleAR
import sys
from colores import *

def crear_botones(n):
	return [[sg.Button("A",font=("Impact", 12),size=(4,1),button_color=color_boton)]for i in range(n)]

def juego (cargar=False):
	if sys.platform == "win32":
		layout=[
			[sg.Text("00:00"),sg.Text("texto",size=(60,1),justification="center"),sg.Image(sys.path[0]+"\imagenes\playerlogo2.png"),sg.Text("9999"),sg.Image(sys.path[0]+"\imagenes\computerlogo2.png"),sg.Text("9999"),sg.Text("0:00"), sg.Button("Iniciar",size=(15,2),font=("Impact", 12),button_color=color_boton2)],
			[sg.Column(crear_botones(15)) for i in range(15)],
			[sg.Button("Confirmar",size=(28,2),font=("Impact", 11),button_color=color_boton2),sg.Button("Pasar",size=(28,2),font=("Impact", 11),button_color=color_boton2),sg.Button("Posponer",size=(28,2),font=("Impact", 11),button_color=color_boton2),sg.Button("Terminar",size=(28,2),font=("Impact", 11),button_color=color_boton2)],
			[sg.Button("A",font=("Impact", 18),size=(9,1),button_color=color_boton)for i in range(7)], 
			[sg.Text("Letras en la bolsa: N",size=(80,1)), sg.Button("Cambiar (N)",size=(25,2),font=("Impact", 12),button_color=color_boton2)]
			]
	elif sys.platform == "linux":
		layout=[
			[sg.Text("00:00"),sg.Text("texto",size=(60,1),justification="center"),sg.Image(sys.path[0]+"/imagenes/playerlogo2.png"),sg.Text("9999"),sg.Image(sys.path[0]+"/imagenes/computerlogo2.png"),sg.Text("9999"),sg.Text("0:00"), sg.Button("Iniciar",size=(15,2),font=("Impact", 12),button_color=color_boton2)],
			[sg.Column(crear_botones(15)) for i in range(15)],
			[sg.Button("Confirmar",size=(28,2),font=("Impact", 11),button_color=color_boton2),sg.Button("Pasar",size=(28,2),font=("Impact", 11),button_color=color_boton2),sg.Button("Posponer",size=(28,2),font=("Impact", 11),button_color=color_boton2),sg.Button("Terminar",size=(28,2),font=("Impact", 11),button_color=color_boton2)],
			[sg.Button("A",font=("Impact", 18),size=(9,1),button_color=color_boton)for i in range(7)], 
			[sg.Text("Letras en la bolsa: N",size=(80,1)), sg.Button("Cambiar (N)",size=(25,2),font=("Impact", 12),button_color=color_boton2)]
			]
	else:
		layout=[
			[sg.Text("00:00"),sg.Text("texto",size=(60,1),justification="center"),sg.Text("9999"),sg.Text("9999"),sg.Text("0:00"), sg.Button("Iniciar",size=(15,2),font=("Impact", 12),button_color=color_boton2)],
			[sg.Column(crear_botones(15)) for i in range(15)],
			[sg.Button("Confirmar",size=(28,2),font=("Impact", 11),button_color=color_boton2),sg.Button("Pasar",size=(28,2),font=("Impact", 11),button_color=color_boton2),sg.Button("Posponer",size=(28,2),font=("Impact", 11),button_color=color_boton2),sg.Button("Terminar",size=(28,2),font=("Impact", 11),button_color=color_boton2)],
			[sg.Button("A",font=("Impact", 18),size=(9,1),button_color=color_boton)for i in range(7)], 
			[sg.Text("Letras en la bolsa: N",size=(80,1)), sg.Button("Cambiar (N)",size=(25,2),font=("Impact", 12),button_color=color_boton2)]
			]

	if cargar:
		layout[0][1]=sg.Text("Juego cargado, pulse iniciar para retomar.",size=(60,1),justification="center")
	else:
		layout[0][1]=sg.Text("Pulse iniciar para comenzar un nuevo juego.",size=(60,1),justification="center")

	
	window = sg.Window("ScrabbleAR",layout)

	while True:
		evento, valores= window.read()
		if evento == sg.WIN_CLOSED: 
			break

	window.Close()


