class Arma():
	def __init__ (self, ATK, Nome, Descricao):
		self.ATK = ATK
		self.Nome = Nome
		self.Descricao = Descricao



armaTemplate = Arma(ATK = 1, Nome = "Template", Descricao = "Template")

espada = Arma(ATK= 10, Nome="Espada de madeira", Descricao="Espada inicial")

cajado = Arma(ATK= 5, Nome="Cajado inicial", Descricao="cajado inicial")

arco = Arma(ATK= 8, Nome="Arco simples", Descricao="Arco inicial")




dict_Arma = {0:armaTemplate, 1:espada, 2:cajado, 3:arco}