#!/usr/bin/python3
# -*- coding: utf-8 -*-

from math import pow as potencia
from math import sqrt as raiz
from pathlib import Path
from pickle import dump, load
from datetime import datetime


def punto_circulo():
	centro = (0,0)
	radio = float(input('Radio: '))
	x = float(input('Coordenada X del punto: '))
	y = float(input('Coordenada Y del punto: '))

	hipotenusa = raiz(( potencia(x,2) + potencia(y,2)))

	if hipotenusa <= radio:
		pertenece = True
		print(f'El punto P({x},{y}) se encuentra al \
			interior del círculo con centro en el origen y radio {radio}')
	else:
		pertenece = False
		print(f'El punto P({x},{y}) NO se encuentra al \
			interior del círculo con centro en el origen y radio {radio}')	

def palindromes():
	s1='amor a Roma'
	s2='Anita atina'
	s3='la tele letal'
	s4='Dábale arroz a la zorra el abad'
	s5='Anula las alas a la luna'
	s6='Isaac no ronca ası́'
	s7='Anita, la latina'

	s11 = s1[::-1]
	print(s1)
	print(s11)
	# Operador ternario
	check_palindrome = True if s1==s11 else False
	print(check_palindrome)


def vocales():
	f_process = 'python_es.txt'
	f_results = 'vocales_linea.txt'
	f_serialization = '__vocales.pkl'
	set_vocales = {'a', 'e', 'i', 'o', 'u', 'á', 'é', 'í',\
					'ó', 'ú', 'ü'}
	pwd = Path.cwd()
	p = Path('.')

	# Ruta a los archivos
	f_results_p = Path(p / f_results)
	f_process_p = Path(p / f_process)
	f_serialization_p = Path(p / f_serialization)

	# Contenidos de los directorios
	dirs = [str(x) for x in p.iterdir() if x.is_dir()]
	s_dirs = "\n".join(dirs)
	dirs_s = "\n".join
	files = [str(x) for x in list(p.glob('**/*.py'))]
	s_files = "\n".join(files)

	print(f'USTED ESTÁ AQUÍ:\n{pwd}\n')
	print(f'DIRECTORIOS:\n{s_dirs}\n')
	print(f'ARCHIVOS PYTHON:\n{s_files}\n')
	
	# Si no existe el archivo de resultados, lo crea.
	if not f_results_p.exists():
		f_results_p.touch()

	# Si existe el archivo que vamos a procesar, empezamos el proceso.
	if f_process_p.exists():

		# Información sobre el tamaño del archivo
		print(f'Tamaño del archivo: {f_process_p.stat().st_size} bytes')

		# Inicialización de la información del puntero de lectura
		serialization_dict = {'pointer':0, 'lines':0}

		# Si no existe el archivo de serialización, lo crea; si existe, carga
		# su información.
		if f_serialization_p.exists():
			with f_serialization_p.open(mode='rb') as f_ser:
				serialization_dict = load(f_ser)
		else:
			f_serialization_p.touch()
			with f_serialization_p.open(mode='wb') as f_ser:
				dump(serialization_dict, f_ser)
			
		print(serialization_dict)
		# Abre el archivo a procesar, y lo procesa.
		t = datetime.now()
		with f_process_p.open(mode='r', encoding="utf-8") as f:

			# Ubica el puntero de lectura en el lugar donde quedó en la
			# llamada pasada al script.
			f.seek(serialization_dict['pointer'],0)
			
			# Lee una línea (diferente a una línea vacía) y actualiza los punteros.
			while True:
				linea = f.readline()
				serialization_dict['pointer'] = f.tell()
				serialization_dict['lines'] = serialization_dict['lines']+1
				if ((linea == "") or (linea == "\n")): continue
				else: break
			
			# Procesa la línea
			ll = linea.split(" ")
			func_filtro = lambda x: len(set(x)&set_vocales)>=2
			dos_o_mas = list(filter(func_filtro, ll))

			print('\n--------------------------')
			print(f'Long.Linea: {len(linea)}')
			print(f'Puntero: {serialization_dict["pointer"]}')
			print(linea)
			print(dos_o_mas)
			
			# Incluye los nuevos resultados en el archivo de resultados
			with f_results_p.open(mode='a+', encoding="utf-8") as f_res:
				f_res.write(f'{t}\tLínea:{serialization_dict["lines"]} {dos_o_mas}\n')

			# Actualiza el archivo de serialización del diccionario
			with f_serialization_p.open(mode='wb') as f_ser:
				dump(serialization_dict, f_ser)

	else:
		print(f'ERROR: El archivo {f_process} no está en la ruta especificada.\
			\n{str(f_process_p)}')


if __name__ == '__main__':
	#punto_circulo()
	#palindromes()
	vocales()