# Horarios
def pegaDIA(h):
	i = 0
	dias = [0,'domingo','segunda','terça','quarta','quinta','sexta','sábado']
	retorno = []
	while( h[i].isdigit() == True ):
		retorno.append( dias[int(h[i])] )
		i += 1
	h = h[i:len(h)]
	return retorno


def pegaTURNO(h):
	retorno = []
	for i in range(len(h)):
		if h[i].isalpha() == True:
			if h[i] == 'M':
				retorno.append('Manhã') 
			elif h[i] == 'T':
				retorno.append('Tarde') 
			else:
				retorno.append('Noite')
			break
	retorno.append(i+1)
	return retorno


def pegaHORA_manha(h):
	horas = [0,6, 7, 8, 9, 10, 11]
	return horas[ int(h) ]

def pegaHORA_tarde(h):
	horas = [0,12, 13, 14, 15, 16, 17]
	return horas[ int(h) ]

def pegaHORA_noite(h):
	horas = [0,18, 19, 20, 21]
	return horas[ int(h) ]


def pegaHORA(h, turno):
	horas = []
	while turno[1] < len(h):
		if turno[0] == 'Manhã':
			horas.append(pegaHORA_manha(h[turno[1]]))
		elif turno[0] == 'Tarde':
			horas.append(pegaHORA_tarde(h[turno[1]]))
		else:
			horas.append(pegaHORA_noite(h[turno[1]]))
		turno[1] += 1

	return horas



def pegaHORARIOS(lista):
	retorno = []

	for i in lista:
		dia = pegaDIA(i)
		turno = pegaTURNO(i)
		hora = pegaHORA(i, turno)
		aula = {
			'dia': dia,
			'turno': turno[0],
			'hora': hora
		}
		retorno.append(aula)

	return retorno


def apresenta(horarios):
	for i in horarios:
		print('-' * 50)
		print('DIAS: ')
		for j in i['dia']:
			print('|\t{}'.format(j.upper()))
		
		print('TURNO: ')
		print('|\t{}'.format(i['turno']))

		print('HORAS: ')
		for k in i['hora']:
			print('|\t{}:00 até as {}:00'.format(k, k+1))
	print('-' * 50)


h = str(input('Digite o horario: '))
# h = '56T456'
lista = h.split(' ')
horarios = pegaHORARIOS(lista)
apresenta(horarios)


