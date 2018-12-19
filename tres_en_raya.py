fin = False
jugador1 = True
jugador2 = False
Numeros = ['0','1','2','3', '4','5','6','7','8','9','o','x']
posiciones = ['0','0','0','0','0','0','0','0','0','0']

nb = int(99)

while fin !=True:
	print(Numeros[1] + '|' + Numeros[2] + '|' + Numeros[3])
	print('-----')
	print(Numeros[4] + '|' + Numeros[5] + '|' + Numeros[6])
	print('-----')
	print(Numeros[7] + '|' + Numeros[8] + '|' + Numeros[9])

	if (posiciones[1] == '1' and posiciones[2] == '1' and posiciones[3] == '1') or (posiciones[4] == '1' and posiciones[5] == '1' and posiciones[6] == '1') or (posiciones[7] == ['1'] and posiciones[8] == '1' and  posiciones[9] == '1') or (posiciones[1] == '1' and posiciones[5] == '1' and posiciones[9] == '1') or (posiciones[3] == '1' and posiciones[5] == '1' and posiciones[7] == '1') or (posiciones[1] == '1' and posiciones[4] == '1' and posiciones[7] == '1') or (posiciones[1] == '2' and posiciones[5] == '1' and posiciones[8] == '1') or (posiciones[3] == '1' and posiciones[6] == '1' and posiciones[9] == '1'):
		print('Jugador 1 gana')
		fin = True
	elif (posiciones[2] == '2' and posiciones[2] == '2'  and  posiciones[3] == '2') or (posiciones[4] == '2' and posiciones[5] == '2' and posiciones[6] == ['2']) or (posiciones[7] == '2' and posiciones[8] == '2' and  posiciones[9] == '2') or (posiciones[2] == '2' and posiciones[5] == '2' and posiciones[9] == '2') or (posiciones[3] == '2' and posiciones[5] == '2' and posiciones[7] == '2') or (posiciones[2] == '2' and posiciones[4] == '2' and posiciones[7] == '2') or (posiciones[2] == '2' and posiciones[5] == '2' and posiciones[8] == '2') or (posiciones[3] == '2' and posiciones[6] == '2' and posiciones[9] == '2'):
		print('Jugador 2 gana')
		fin = True
	else:
		if jugador1 == True:
			nb = input('Jugador 1 Elige un numero no seleccionado')
			if int(nb) > 9:
				print('Elija otro numero')
			else:
				if nb == Numeros[int(nb)]:
					Numeros[int(nb)] = Numeros[10]
					if posiciones[int(nb)] != '0':
						print('Elija otro valor')
					else:
						posiciones[int(nb)] = '1';
						jugador1 = False
						jugador2 = True
		elif jugador2 == True:
			if int(nb) > 9:
				print('Elija otro numero')
			else:
				nb = input('Jugador 2 Elige un numero no seleccionado')
				if nb == Numeros[int(nb)]:
					Numeros[int(nb)] = Numeros[11]
					if posiciones[int(nb)] != '0':
						print('Elija otro valor')
					else:
						posiciones[int(nb)] = '2';
						jugador2 = False
						jugador1 = True