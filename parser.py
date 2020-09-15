"""
Create by John Mello
Simple argument parser
"""
import sys
host = ''
port = 0
class parseError(Exception):
	def __init__(self, message):
		self.message = message
	def __str__(self):
		return self.message
"""
Retorna uma lista de truplas contendo o argumento, e seu valor.
"""
def parser(args, options, f=''):
	r = []
	# Transformamos a string "options" em um array com str.split()
	options = options.split(',')
	# Aqui são os argumentos facultativos
	f = f.split(',')
	# Laço que itera com todos os itens da lista
	for arg in args:
		# Se o elemento estiver dentro das opções passadas pelo usuário
		if arg in options:
			try:
				# Tenta adicionar uma trupla ao array
				r.append((arg, args[args.index(arg) + 1]))
			except IndexError:
				# Caso o usuário não forneça a opção, o array não será indexado corretamente.
				# Então lançamos uma excepção
				raise parseError('error: %s require argument.'%arg)
		# Aqui, apenas adicionamos os argumentos facultativos, caso estiverem na lista
		elif arg in f:
			r.append((arg, ''))
		elif not arg in options and not arg in f and arg.startswith('-'):
			raise parseError('error: %s not incognized.'%arg)
	return r
try:
	opts = parser(sys.argv[1:], '-h,-p', '-l')
except Exception as err:
	print(err)
for key, value in opts:
	if key == '-h':
		host = value
	elif key == '-p':
		port = value
	else:
		pass
print('Host: %s; Port: %d'%(host, int(port)))