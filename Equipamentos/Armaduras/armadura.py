class Armadura():
	def __init__ (self, DEF, Nome, Descricao):
		self.DEF = DEF
		self.Nome = Nome
		self.Descricao = Descricao


ArmaduraTemplate = Armadura(DEF = 0, Nome = "Template", Descricao = "Template")

peitoralcouro = Armadura(DEF= 10, Nome="Peitoral de Couro", Descricao="Peitoral inicial")

mantomagico = Armadura(DEF= 15, Nome="Manto Magico", Descricao="Manto com capacidades mágicas")

capuz = Armadura(DEF= 5, Nome="Capuz", Descricao="Capuz capaz de disfarçar-se na floresta")





dict_Armadura = {0:ArmaduraTemplate, 1:peitoralcouro, 2:mantomagico, 3:capuz}